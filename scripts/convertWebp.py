from PIL import Image
import os

def convert_images_to_webp(folder_path, quality=60):
    if not os.path.isdir(folder_path):
        print(f"Invalid folder path: {folder_path}")
        return
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.webp")
            
            try:
                with Image.open(image_path) as img:
                    img.save(output_path, 'WEBP', quality=quality)
                    print(f"Converted: {filename} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    folder_path = r"C:\Users\MI\Desktop\mekomimi.github.io\img"  # 请替换为你的实际文件夹路径
    convert_images_to_webp(folder_path, quality=60)
