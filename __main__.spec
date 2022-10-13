# -*- mode: python -*-
a = Analysis(['__main__.py'],
             pathex=['C:\\Users\\Mastermind\\Dropbox\\moongate\\juros'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\__main__', 'jurosapp.exe'),
          debug=False,
          strip=None,
          upx=False,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=False,
               name=os.path.join('dist', '__main__'))
