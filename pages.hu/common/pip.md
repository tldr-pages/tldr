# pip

> Python csomagkezelő. Néhány alparancsnak, mint például a `pip install`, saját használati dokumentációja van. További információ: <https://pip.pypa.io>.

- Telepítsen egy csomagot (további telepítési példákért lásd: `pip install` ):

`pip install {{package_name}}`

- Egy csomag telepítése a felhasználó könyvtárába a rendszerszintű alapértelmezett hely helyett:

`pip install --user {{package}}`

- Egy csomag frissítése:

`pip install --upgrade {{package_name}}`

- Egy csomag eltávolítása:

`pip uninstall {{package_name}}`

- Telepített csomagok mentése fájlba:

`pip freeze > {{requirements.txt}}`

- Telepített csomagok adatainak megjelenítése:

`pip show {{package_name}}`

- Csomagok telepítése fájlból:

`pip install --requirement {{requirements.txt}}`
