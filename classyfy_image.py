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

# Example usage
image_list = [
    "./img/Einstein.jpg", 
    "./img/Einstein2.jpg", 
    "./img/Einstein3.jpg",
    './img/cap1.png', 
    './img/cap2.png', 
    './img/capture.png'
]
result = classify_images(image_list)
print(result)
