from cx_Freeze import setup, Executable

base = None    

executables = [Executable("src.py", base=base)]

packages = ["idna", 'os', 'ctypes', 'PIL', 'pathlib', 'shutil']
options = {
    'build_exe': {    
        'packages':packages,
    },    
}
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

setup(
    name = "Spotlight_Wallpaper_gen",
    options = options,
    version = "1.0",
    description = 'generates wallpaper from spotlight images',
    executables = executables
), 
