# elen_project_setup.py

import os

def setup_environment():
    """Set up the project environment."""
    # Create directories
    directories = ['data', 'notebooks', 'scripts', 'results']
    for dir_name in directories:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Created directory: {dir_name}")

    # Create a requirements.txt file
    with open('requirements.txt', 'w') as f:
        f.write("pandas\n")
        f.write("numpy\n")
        f.write("matplotlib\n")
        print("Created requirements.txt with basic dependencies.")

if __name__ == "__main__":
    setup_environment()