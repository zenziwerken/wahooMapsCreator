# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['wahoo_map_creator.py'],
             pathex=['/Users/benjamin/VSCode/wahooMapsCreator'],
             binaries=[],
             datas=[( 'common_resources', 'common_resources' )],
             hiddenimports=['requests', 'gdal', 'geojson', 'shapely'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='wahoo_map_creator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wahoo_map_creator')
