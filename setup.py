from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('mainwindow.py', base=base, target_name = 'VivaTodo', icon = 'app.ico')
]

setup(name='Viva-Todo',
      version = '1.0',
      description = 'Viva Task Management',
      options = {'build_exe': build_options},
      executables = executables)
