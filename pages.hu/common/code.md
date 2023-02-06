# code

> Platformokon átívelő és bővíthető kódszerkesztő. További információ: <https://github.com/microsoft/vscode>.

- Indítsa el a Visual Studio Code-ot:

`code`

- Meghatározott fájlok/könyvtárak megnyitása:

`code {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Két meghatározott fájl összehasonlítása:

`code --diff {{path/to/file1}} {{path/to/file2}}`

- Meghatározott fájlok/könyvtárak megnyitása új ablakban:

`code --new-window {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Egy adott bővítmény telepítése/eltávolítása:

`code --{{install|uninstall}}-extension {{publisher.extension}}`

- Telepített bővítmények nyomtatása:

`code --list-extensions`

- Telepített bővítmények és verzióik nyomtatása:

`code --list-extensions --show-versions`

- A szerkesztő elindítása szuperfelhasználóként (root), miközben a felhasználói adatokat egy adott könyvtárban tárolja:

`sudo code --user-data-dir {{path/to/directory}}`
