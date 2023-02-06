# pip3

> Python csomagkezelő. További információ: <https://pip.pypa.io>.

- Elérhető csomagok keresése:

`pip3 search {{package_name}}`

- Telepítsen egy csomagot:

`pip3 install {{package_name}}`

- Egy csomag egy adott verziójának telepítése:

`pip3 install {{package_name}}=={{package_version}}`

- Egy csomag frissítése:

`pip3 install --upgrade {{package_name}}`

- Egy csomag eltávolítása:

`pip3 uninstall {{package_name}}`

- A telepített csomagok listájának mentése egy fájlba:

`pip3 freeze > {{requirements.txt}}`

- Csomagok telepítése fájlból:

`pip3 install --requirement {{requirements.txt}}`

- Telepített csomagok adatainak megjelenítése:

`pip3 show {{package_name}}`
