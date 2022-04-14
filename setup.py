import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "PyDracula",
    version = "1.0",
    description = "Autonomous car control applications",
    author = "CacheHit Team - Ho Chi Minh City University of Technology",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
