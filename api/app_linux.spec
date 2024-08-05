# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files, get_package_paths
import os
import sys

#Para descobrir a localização no seu sistema: "find /usr -name 'libpython3.10.so'"
python_lib = '/usr/lib/python3.10/config-3.10-x86_64-linux-gnu'

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[
        (python_lib, os.path.basename(python_lib))  # Inclua a biblioteca compartilhada do Python
    ],
    datas = [
        ('/mnt/c/Users/joand/PycharmProjects/AutomTest/assets', 'assets'),
        ('/mnt/c/Users/joand/PycharmProjects/AutomTest/environment', 'environment'),
        ('/mnt/c/Users/joand/PycharmProjects/AutomTest/dependencies', 'dependencies'),
         *collect_data_files('flask')
    ],
    hiddenimports=['flask', *collect_submodules('flask'), 'flask_cors', 'openai', 'google.generativeai', 'unidecode', 'spacy', 'pt_core_news_md'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='automtest_backend',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
