# atom

> Egy platformokon átívelő, bővíthető szövegszerkesztő. A bővítményeket a `apm` kezeli. További információ: <https://atom.io/>.

- Fájl vagy könyvtár megnyitása:

`atom {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár megnyitása új ablakban:

`atom -n {{path/to/file_or_directory}}`

- Fájl vagy könyvtár megnyitása egy meglévő ablakban:

`atom --add {{path/to/file_or_directory}}`

- Atom megnyitása biztonságos módban (nem tölt be további csomagokat):

`atom --safe`

- Megakadályozza, hogy az Atom elágazás a háttérbe kerüljön, az Atom a terminálhoz csatolva marad:

`atom --foreground`

- Várja meg, hogy az Atom ablak bezáródjon, mielőtt visszatérne (hasznos a Git commit szerkesztőhöz):

`atom --wait`
