from PIL import Image
import imagehash

def classify_images(image_paths):
    image_groups = {}

    for img_path in image_paths:
        print(f"Processing: {img_path}")  # Debugging step
        try:
            img = Image.open(img_path)
            img = img.resize((256, 256))  # Resize for efficiency
            hash_key = str(imagehash.phash(img))

        except Exception as e:
            print(f"Error with {img_path}: {e}")
            continue

        if hash_key in image_groups:
            image_groups[hash_key].append(img_path)
            # print("Image added to group, list = ", image_groups[hash_key])
            #copy the images to the existing folder
        else:
            image_groups[hash_key] = [img_path]
            # print("new Image added to group list = ", image_groups[hash_key])
            # create a new folder and copy the images to the

    return image_groups

def group_into_folders(image_groups):
    """
    image_groups: dictionary of image groups
    image_groups = {
        'k_1' : ['img1.jpg', 'img2.jpg'],
        'k_2' : ['img3.jpg', 'img4.jpg'],
        'k_3' : ['img5.jpg', 'img6.jpg'],
    }
    """
    for key in image_groups:
        folder_name = f"Group_{key}"
        print(f"Creating folder: {folder_name}")

        for img_path in image_groups[key]:
            print(f"\tCopying {img_path} to {folder_name}")

        # Create the folder
        # Copy the images to the folder
        # Create a text file with the image paths
        # Create a text file with the image hashes


# Example usage
image_list = [
    "./img/Einstein.jpg", 
    "./img/Einstein2.jpg", 
    "./img/Einstein3.jpg",
    './img/cap1.png', 
    './img/cap2.png', 
    './img/capture.png'
]
my_dict = classify_images(image_list)
print(my_dict)

group_into_folders(my_dict)