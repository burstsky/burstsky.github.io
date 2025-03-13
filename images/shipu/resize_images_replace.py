#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
图片大小调整脚本（直接替换原图）
将当前目录下的所有jpg图片调整为统一大小：2544x3464
"""

import os
from PIL import Image
import sys
import shutil
import time

# 目标尺寸
TARGET_WIDTH = 2544
TARGET_HEIGHT = 3464

def resize_image(image_path, target_width, target_height):
    """
    调整图片大小并直接替换原图
    
    参数:
        image_path (str): 图片路径
        target_width (int): 目标宽度
        target_height (int): 目标高度
    """
    try:
        # 创建临时文件路径（使用相同的扩展名）
        file_name, file_ext = os.path.splitext(image_path)
        temp_path = f"{file_name}_temp{file_ext}"
        
        # 打开图片
        with Image.open(image_path) as img:
            # 获取原始图片尺寸
            original_width, original_height = img.size
            
            # 如果图片已经是目标尺寸，则跳过
            if original_width == target_width and original_height == target_height:
                print(f"跳过 {os.path.basename(image_path)} - 已经是目标尺寸")
                return
            
            # 创建一个新的白色背景图片
            new_img = Image.new("RGB", (target_width, target_height), "white")
            
            # 调整原图大小，保持比例
            img_ratio = original_width / original_height
            target_ratio = target_width / target_height
            
            if img_ratio > target_ratio:
                # 图片比目标更宽，以宽度为基准调整
                new_width = target_width
                new_height = int(new_width / img_ratio)
            else:
                # 图片比目标更高，以高度为基准调整
                new_height = target_height
                new_width = int(new_height * img_ratio)
            
            # 调整图片大小，使用高质量的重采样滤镜
            # 在不同版本的Pillow中，重采样滤镜的常量名称可能不同
            # 使用整数值代替常量名称（1=LANCZOS, 3=BICUBIC）
            resized_img = img.resize((new_width, new_height), 1)  # 1 对应 LANCZOS/ANTIALIAS
            
            # 计算居中位置
            paste_x = (target_width - new_width) // 2
            paste_y = (target_height - new_height) // 2
            
            # 将调整后的图片粘贴到新图片上
            new_img.paste(resized_img, (paste_x, paste_y))
            
            # 保存到临时文件
            new_img.save(temp_path, format="JPEG", quality=95)
            
            # 替换原文件
            shutil.move(temp_path, image_path)
            
            print(f"已调整: {os.path.basename(image_path)} ({original_width}x{original_height} -> {target_width}x{target_height})")
            
    except Exception as e:
        print(f"处理 {image_path} 时出错: {e}")
        # 如果临时文件存在，则删除
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass

def main():
    """
    主函数，处理当前目录下的所有jpg图片
    """
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取所有jpg文件
    image_files = [f for f in os.listdir(script_dir) if f.lower().endswith('.jpg')]
    
    if not image_files:
        print("当前目录下没有找到jpg图片")
        return
    
    # 排除脚本自身
    image_files = [f for f in image_files if not f.startswith('resize_images')]
    
    print(f"找到 {len(image_files)} 个jpg图片，开始处理...")
    
    # # 创建备份目录
    # backup_dir = os.path.join(script_dir, f"backup_{int(time.time())}")
    # os.makedirs(backup_dir)
    # print(f"创建备份目录: {backup_dir}")
    
    # # 备份原始图片
    # for image_file in image_files:
    #     image_path = os.path.join(script_dir, image_file)
    #     backup_path = os.path.join(backup_dir, image_file)
    #     shutil.copy2(image_path, backup_path)
    
    # print("已备份所有原始图片")
    
    # 处理每个图片
    for image_file in image_files:
        image_path = os.path.join(script_dir, image_file)
        resize_image(image_path, TARGET_WIDTH, TARGET_HEIGHT)
    
    print("处理完成！所有图片已调整为目标尺寸")
    # print(f"原始图片备份在: {backup_dir}")

if __name__ == "__main__":
    main() 