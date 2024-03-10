import tkinter as tk
from tkinter import Button, Label, Entry, filedialog, ttk
import os
import shutil


# 初始化 APP 窗口
app = tk.Tk()  
app.title("⛰️ 图片复制工具") # 设置窗口标题


# 显示一个等待加载的文字
status_label = tk.Label(app, text="⏰ 等待开始...", fg="blue")
status_label.grid(row=2, column=0, columnspan=3) # 等待状态标签
 



# 浏览文件夹
def browse_folder(folder_dir):
	folder_selected = filedialog.askdirectory() # 让用户选择要查找文件的文件夹, filedialog 是 tkinter UI 框架, 会弹出一个文件夹选择框
	if folder_selected:
		folder_dir.set(folder_selected) # 👈 将用户选择的文件夹路径, 设置到 folder 变量中 (source_dir 或 target_dir)
		print("路径:", folder_dir.get())  # 确认路径是否已正确设置
		# update_ui() # 执行回调函数 (传入的函数, 也就是 update_ui)


# 开始复制文件
def start_copy():
	try:
		print("🚀 开始复制文件")
		source = source_dir.get()  # 使用 .get() 方法获取路径字符串
		target = target_dir.get()  # 使用 .get() 方法获取路径字符串
		type = selected_file_type.get()  # 获取文件类型
		if not os.path.exists(target): # 如果【目标目录】不存在
			os.makedirs(target) # 创建【目标目录】文件夹
		# 遍历原始目录
		for root, dirs, files in os.walk(source):
			for file in files:
				if file.endswith(type): # 检查看后缀是否是 .png 文件
					# 拼接【源文件】的完整路径
					origin_src = os.path.join(root, file)
					# 构建【目标文件】的完整路径
					copy_file_src = os.path.join(target, file) # 传入【目标目录】和【文件名】
					# 复制【原始文件的路径】到【目标文件的路径】
					shutil.copy(origin_src, copy_file_src)
					status_label.config(text=f'已复制一个文件：{file}')
					print(f'👍 已复制一个文件：{file}')
		print('✅ 复制完成')
	except Exception as e:
		print(f'复制过程中发生错误: {e}')
  
  


# 窗口居中显示
appWidth = 700 # 应用宽度
appHeight = 360 # 应用高度
screen_width = app.winfo_screenwidth() # 获取系统屏幕宽度跟高度, 计算中央值
screen_height = app.winfo_screenheight() # 获取系统屏幕宽度跟高度, 计算中央值
x = int((screen_width - appWidth) / 2)
y = int((screen_height - appHeight) / 2)
app.geometry(f'{appWidth}x{appHeight}+{x}+{y}') # 设置窗口大小和位置, geometry 方法表示【宽度 x 高度 + X + Y】



# 👇 浏览源目录, command = XXX 为函数的调用
source_dir = tk.StringVar()  # StringVar 需要通过 .get() 方法获取值, # 🔥🔥 使用 【StringVar 变量】绑定【输入】跟【输出】的文件夹路径
tk.Entry(app, textvariable=source_dir).grid(row=0, column=1)
tk.Button(app, text="选择源文件", command=lambda: browse_folder(source_dir)).grid(row=0, column=2) # 创建一个用于触发【浏览文件夹】的按钮


# 👇 选择目标, command = XXX 为函数的调用, # 🔥🔥 使用 【StringVar 变量】绑定【输入】跟【输出】的文件夹路径
target_dir = tk.StringVar()  # StringVar 需要通过 .get() 方法获取值
tk.Entry(app, textvariable=target_dir).grid(row=0, column=3)
tk.Button(app, text="选择目标文件", command=lambda: browse_folder(target_dir)).grid(row=0, column=3) # 创建一个用于触发【浏览文件夹】的按钮


# 文件格式下拉菜单
file_types = ('.png', '.jpeg', '.pdf')
selected_file_type = tk.StringVar()
selected_file_type.set(file_types[0]) # 设置默认值
file_type_menu = tk.OptionMenu(app, selected_file_type, *file_types)
file_type_menu.grid(row=0, column=5)

# 🔥 开始复制文件, command = XXX 为函数的调用
tk.Button(app, text="开始复制", command=start_copy).grid(row=2, column=2, columnspan=4, sticky='ew') # 创建一个用于触发【复制文件】的按钮




# 启动主窗口
app.mainloop() 




# import tkinter as tk
# from tkinter import ttk

# app = tk.Tk()
# app.title("Demo App")

# frame = ttk.Frame(app)
# frame.pack(fill='both', expand=True)

# label = ttk.Label(frame, text="Hello, Tkinter!")
# label.pack()

# app.mainloop()
