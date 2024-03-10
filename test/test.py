import tkinter as tk

# 测试
def test_tkinter():
    # 创建主窗口
    root = tk.Tk()
    root.title("Tkinter 测试")

    # 创建一个标签 (Label) 控件，显示文本
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=20)  # pady 是上下边距

    # 启动事件循环
    root.mainloop()

if __name__ == "__main__":
    test_tkinter()