# pip install

> Python csomagok telepítése. További információ: <https://pip.pypa.io>.

- Telepítsen egy csomagot:

`pip install {{package_name}}`

- Egy csomag egy adott verziójának telepítése:

`pip install {{package_name}}=={{package_version}}`

- Egy fájlban felsorolt csomagok telepítése:

`pip install --requirement {{path/to/requirements.txt}}`

- Csomagok telepítése URL-címről vagy helyi fájlarchívumból (.tar.gz | .whl):

`pip install --find-links {{url|path/to/file}}`

- Helyi csomag telepítése az aktuális könyvtárba develop (szerkeszthető) módban:

`pip install --editable {{.}}`
