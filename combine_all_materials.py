import os
from PIL import Image

print()

def delete_images(image_paths):

    filtered_image_paths = [list_img for list_img in image_paths if 'overlayed' not in list_img]

    for img_path in filtered_image_paths:
        try:
            os.remove(img_path)
            print(f"Deleted {img_path}")
        except Exception as e:
            print(f"Error deleting {img_path}: {e}")




def overlay_images_by_channel(image_paths):
    base_image = Image.open(image_paths[0])

    for image_path in image_paths[1:]:
        overlay_image = Image.open(image_path)
        base_image.paste(overlay_image, (0, 0), overlay_image.convert("RGBA").split()[3])  

    return base_image    


def overlay_images(Path):

    list_of_image_file_paths = []
    list_images = []

    for image_file in os.listdir(Path):
        
        if image_file.endswith(('.png', '.jpg', '.jpeg')):

            list_images.append(image_file)

            string = image_file
            last_dot_index = string.rfind(".")
            substring = string[:last_dot_index]
            name_channel = substring.split('_')[-1]


            list_of_image_file_paths.append(name_channel)

    unique_list = list(set(list_of_image_file_paths))
    list_of_image_file_paths = {item: [] for item in unique_list}

    for image in list_images:
        parts = image.split('_')
        channel_type = parts[-1].split('.')[0]  
        list_of_image_file_paths[channel_type].append(image)


    for group, image_paths in list_of_image_file_paths.items():

        print(f"Overlaying images for {group} group!")
        
        result_image = overlay_images_by_channel(image_paths)

        result_image.save(f"overlayed_{group}.png")
        print(f"\tSaved overlayed image for {group}: overlayed_{group}.png\n")

    
    delete_images(list_images)


overlay_images(os.getcwd())

