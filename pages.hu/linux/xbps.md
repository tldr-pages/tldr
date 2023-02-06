# xbps

> Az X Binary Package System (vagy xbps) a Void Linux által használt bináris csomagrendszer. További információ: <https://github.com/void-linux/xbps>.

- Csomagok telepítése és szinkronizálása a távoli tárolóval:

`xbps-install --sync {{package_name1}} {{package_name2}}`

- Keressen egy csomagot a távoli tárolóban:

`xbps-query --repository -s {{package_name}}`

- Egy csomag eltávolítása, az összes függőségének telepítve hagyásával:

`xbps-remove {{package_name}}`

- Egy csomag és minden olyan függőségének rekurzív eltávolítása, amelyet más csomagok nem igényelnek:

`xbps-remove --recursive {{package_name}}`

- Az adattár adatbázisainak szinkronizálása, valamint a rendszer és a függőségek frissítése:

`xbps-install --sync --update`

- Távolítsa el a függőségként telepített, de jelenleg nem szükséges csomagokat:

`xbps-remove --remove-orphans`

- Az elavult csomagok eltávolítása a gyorsítótárból:

`xbps-remove --clean-cache`
