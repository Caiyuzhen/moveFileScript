import os
import shutil


# 源目录
source_dir = '/Users/userName/Desktop/fluentui-emoji-main'

# 目标输出目录
target_dir = '/Users/userName/Desktop/pngResult'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    
# 遍历源目录
for root, dirs, files in os.walk(source_dir):
	# 检查是否叫 3D
	if '3D' in root:
		for file in files:
			if file.endswith('.png'): # 检查看后缀是否是 .png 文件
				# 拼接【源文件】的完整路径
				origin_src = os.path.join(root, file)
				# 构建【目标文件】的完整路径
				copy_file_src = os.path.join(target_dir, file) # 传入【目标目录】和【文件名】
				# 复制【原始文件的路径】到【目标文件的路径】
				shutil.copy(origin_src, copy_file_src)
				print(f'已复制一个文件: {file}')
    
print('✅ 全部复制完成')