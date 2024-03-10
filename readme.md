# 安装依赖
- 使用了 Tkinter 作为简单的 GUI 框架，需要安装 python3 的 Tkinter 库, 键入 `brew reinstall python`。
- 打包文件的库 `pip3 install pyinstaller` | `/usr/bin/python3 -m pip install pyinstaller`
- `brew install python-tk` 

# 测试
- `/usr/bin/python3 app.py`

# 打包文件
- `pyinstaller --onefile --windowed app.py` 生成可执行文件。
- 或者使用系统的 python3 进行打包 `/usr/bin/python3 -m PyInstaller --onefile --windowed app.py`
  
# 打开文件
- 打开 dist 下的 app 文件即可。

