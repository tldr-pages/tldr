# pipwin

> Egy eszköz nem hivatalos Python csomagok telepítésére Windowson. További információ: <https://github.com/lepisma/pipwin>.

- Az összes letölthető csomag listája:

`pipwin list`

- Csomagok keresése:

`pipwin search {{partial_name|name}}`

- Telepítsen egy csomagot:

`pipwin install {{package_name}}`

- Egy csomag eltávolítása:

`pipwin uninstall {{package_name}}`

- Egy csomag letöltése egy adott könyvtárba:

`pipwin download --dest {{path/to/directory}} {{package_name}}`

- Csomagok telepítése a `requirements.txt` szerint:

`pipwin install --file {{path/to/requirements.txt}}`
