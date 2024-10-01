import os
import shutil

def build():
    print("Building the application...")

    # Create the build/web directory if it doesn't exist
    os.makedirs('build/web', exist_ok=True)

    # Copy HTML files from templates to build/web
    templates_dir = 'templates'
    build_dir = 'build/web'

    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            src_file = os.path.join(templates_dir, filename)
            dest_file = os.path.join(build_dir, filename)
            shutil.copy(src_file, dest_file)
            print(f"Copied {filename} to {build_dir}")

    print("Build completed successfully.")

if __name__ == "__main__":
    build()
