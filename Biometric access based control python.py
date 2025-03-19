import hashlib
import os
from PIL import Image

def hash_image(image_path):
    """Hashes an image file using SHA-256."""
    try:
        img = Image.open(image_path)
        img_bytes = img.tobytes() # Convert image to bytes
        hasher = hashlib.sha256()
        hasher.update(img_bytes)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None
    except Exception as e: # Catch other potential image errors
        print(f"Error processing image: {e}")
        return None

def create_biometric_template(folder_path):
    """Creates a biometric template from images in a folder."""
    template = {}  # Dictionary to store filename:hash pairs
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')): # Check for image files
            image_path = os.path.join(folder_path, filename)
            hash_value = hash_image(image_path)
            if hash_value: # Only add if hashing was successful
                template[filename] = hash_value
    return template

# Example usage:
image_folder = r"Downloads\archive\SOCOFing\Real"  # Replace with your folder path
biometric_template = create_biometric_template(image_folder)

# Save the template (e.g., to a file):
import json
with open("biometric_template.json", "w") as f:
    json.dump(biometric_template, f, indent=4) # Save in json format

print("Biometric template created and saved.")
