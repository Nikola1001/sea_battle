# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['START.pyw', 'authorization.py', 'bot_ships.py', 'bot_shooting.py', 'checks.py', 'decks.py', 'field.py', 'four_deck_ship.py', 'one_deck_ship.py', 'plr_ships.py', 'settings.py', 'ship.py', 'statistic.py', 'three_deck_ship.py', 'two_deck_ship.py', 'users_data_base.py'],
             pathex=['C:\\Users\\kolag\\Desktop\\sea_battle_final'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='START',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
