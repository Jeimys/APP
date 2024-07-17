from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['D:\\HyperField'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],

    noarchive=False,

    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)


a.datas += [('View\\Wellcome\\Design.kv', 'View\\Wellcome\\Design.kv', 'DATA'),
    ('View\\Menu\\Design.kv', 'View\\Menu\\Design.kv', 'DATA'),
    ('View\\Reading\\Design.kv', 'View\\Reading\\Design.kv', 'DATA'),
    ('View\\Classification\\Design.kv', 'View\\Classification\\Design.kv', 'DATA'),
    ('View\\Result\\Design.kv', 'View\\Result\\Design.kv', 'DATA')]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,Tree('D:\\HyperField\\'),
    a.binaries,
    a.datas, 
    
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
