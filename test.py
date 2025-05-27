import os

def generate_image_list_in_readme(directory_path, readme_file="README.md"):
    """
    Scans a directory for image files and writes their Markdown format
    into a specified README.md file.

    Args:
        directory_path (str): The path to the directory containing images.
        readme_file (str): The name of the README file to write to.
                           Defaults to "README.md".
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.svg')
    image_files = []

    # Collect all image files
    try:
        for item in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, item)):
                if item.lower().endswith(image_extensions):
                    image_files.append(item)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while scanning directory: {e}")
        return

    if not image_files:
        print(f"No image files found in '{directory_path}'.")
        return

    # Prepare Markdown content
    markdown_content = "# Project Images\n\n"
    markdown_content += "Here's a list of images in this project:\n\n"

    for img_name in sorted(image_files): # Sort for consistent order
        # Assuming images are in the same directory as the README or a known path
        # If images are in a subdirectory, adjust the path:
        # relative_image_path = os.path.join("your_image_folder", img_name)
        # For simplicity, we'll assume relative to README or in the same dir
        relative_image_path = os.path.join(os.path.basename(directory_path), img_name) if directory_path != "." else img_name

        # Create the Markdown image line
        markdown_content += f'![{os.path.splitext(img_name)[0]}]({relative_image_path} "{os.path.splitext(img_name)[0]}")\n'

    # Write to README.md
    try:
        with open(readme_file, 'w') as f:
            f.write(markdown_content)
        print(f"Successfully generated '{readme_file}' with {len(image_files)} image entries.")
    except Exception as e:
        print(f"Error writing to '{readme_file}': {e}")

# --- How to Use ---

# 1. Specify the directory containing your images:
#    - To scan the current directory where the script runs:
# image_directory = "."
#    - To scan a specific subfolder (e.g., 'assets'):
# image_directory = "assets"
#    - To scan a specific absolute path:
image_directory = "/home/harsha/Downloads/wallpapers"

# 2. Run the function:
generate_image_list_in_readme(image_directory)
