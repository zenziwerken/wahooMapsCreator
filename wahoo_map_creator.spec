# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

from PyInstaller.utils.hooks import collect_data_files
_osgeo_pyds = collect_data_files('osgeo', include_py_files=True)

osgeo_pyds = []
for p, lib in _osgeo_pyds:
    if '.pyd' in p:
        osgeo_pyds.append((p, ''))

binaries = osgeo_pyds

a = Analysis(['wahoo_map_creator.py', 'tooling/shape2osm.py'],
             pathex=['/Users/benjamin/VSCode/wahooMapsCreator'],
             binaries=binaries,
             datas=[( 'common_resources', 'common_resources' ),
                    ( 'tooling', 'tooling' )],
             hiddenimports=['requests', 'gdal', 'geojson', 'shapely', 'osgeo', 'geos'],
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
