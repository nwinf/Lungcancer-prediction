import os
import shutil

def build():
    print("Building the application...")

    # Create the build/web directory if it doesn't exist
    os.makedirs('build/web', exist_ok=True)

    # Define directories
    templates_dir = 'templates'
    build_dir = 'build/web'

    # List of HTML files to copy
    html_files = ['index.html']  # Add more HTML files as needed

    for filename in html_files:
        src_file = os.path.join(templates_dir, filename)
        dest_file = os.path.join(build_dir, filename)
        if os.path.exists(src_file):
            shutil.copy(src_file, dest_file)
            print(f"Copied {filename} to {build_dir}")
        else:
            print(f"Warning: {src_file} does not exist.")

    print("Build completed successfully.")

if __name__ == "__main__":
    build()
