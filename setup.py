from cx_Freeze import setup, Executable
import sys
import os.path
build_options = {'build_exe':
                    {'includes': ["sqlalchemy", "sqlite3", "PyQt5"],
                     'excludes': ["tkinter"],
                     'include_files': ['CLI SQLite', 'hike.ico'],
                     "icon": r"hike.ico",
                     }}
script = os.path.join("main.py")
if sys.platform == 'win32':
    exe = Executable(script, targetName="HikeDB.exe", base="Win32GUI", copyDependentFiles=True, )
else:
    exe = Executable(script, targetName="HikeDB.exe", base="Win64GUI")
setup(name = "HikeDB",
     version = "1.0",
     description = "Tsislitsky",
     options = build_options,
     executables = [exe],
    )