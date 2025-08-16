from PIL import Image
import os

# 设置文件夹路径和目标宽度
input_folder = r'C:\Users\MI\Desktop\File\mekomimi.github.io'
output_folder = r'C:\Users\MI\Desktop\File\mekomimi.github.io\\resized'
target_width = 400                    # 设置目标宽度
target_height = None                  # 如果保持比例，高度为 None

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 批量调整图片大小
for filename in os.listdir(input_folder):
    if filename.endswith(".webp"):  # 只处理 .webp 文件
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # 保持比例调整尺寸
        width_percent = target_width / float(img.size[0])
        target_height = int((float(img.size[1]) * float(width_percent)))
        
        img_resized = img.resize((target_width, target_height))
        
        # 保存调整后的图片
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)
        print(f"调整完成: {filename}")

print("所有图片已调整完成。")
