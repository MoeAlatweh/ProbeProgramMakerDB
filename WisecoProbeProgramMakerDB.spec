# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2 , glew

block_cipher = None


a = Analysis(['C:\\Users\\malatweh\\PycharmProjects\\WisecoApplications\\ProbeProgramMakerDB\\Main.pyw'],
             pathex=['C:\\Users\\malatweh\\PycharmProjects\\WisecoApplications\\ProbeProgramMakerDB'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='WisecoProbeProgramMakerDB',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\Users\\malatweh\\PycharmProjects\\WisecoApplications\\ProbeProgramMakerDB\\WisecoLogoIcon\\WisecoLogoIcon.ico')
coll = COLLECT(exe, Tree('C:\\Users\\malatweh\\PycharmProjects\\WisecoApplications\\ProbeProgramMakerDB\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='WisecoProbeProgramMakerDB')
