import argparse
import sys
import os

def main():
    """
    Wrapper script to call the main bootstrap logic from the shared tools repository.
    """
    # This dynamically adds the 'infainite.ai.tools' directory to the Python path.
    # It assumes the tools repo is cloned as a sibling to the project repo.
    try:
        # Path to the root of the current project template
        template_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Path to the directory containing all the project folders (the workspace root)
        workspace_root = os.path.dirname(template_dir)
        tools_path = os.path.join(workspace_root, '..', 'infainite.ai.tools')
        
        # A more robust way might be to look for it in common places
        if not os.path.exists(tools_path):
             # Fallback for when the script is run from within the project itself
             workspace_root = os.path.dirname(os.path.dirname(template_dir))
             tools_path = os.path.join(workspace_root, 'infainite.ai.tools')

        if not os.path.exists(tools_path):
            print(f"Error: Tools directory not found at {tools_path}")
            sys.exit(1)

        sys.path.append(os.path.normpath(tools_path))
        
        from bootstrap_workspace import bootstrap

    except ImportError:
        print("Error: Could not import 'bootstrap_workspace'.")
        print("Please ensure the 'infainite.ai.tools' repository is cloned and accessible.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Bootstrap a new client project.")
    parser.add_argument("--client", required=True, help="The name of the client.")
    parser.add_argument("--template", default="swdev-project-template", help="The name of the template to use.")
    args = parser.parse_args()

    bootstrap(args.client, args.template)

if __name__ == "__main__":
    main() 