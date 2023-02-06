# debman

> Man oldalak olvasása a nem telepített csomagokból. További információ: <https://manpages.debian.org/latest/debian-goodies/debman.1.html>.

- Egy megadott csomagnév által biztosított parancs man oldalának olvasása:

`debman -p {{package_name}} {{command_name}}`

- Adja meg a letölteni kívánt csomagverziót:

`debman -p {{package_name}}={{version}} {{command_name}}`

- Man oldal olvasása a `.deb` fájlban:

`debman -f {{path/to/filename.deb}} {{command_name}}`
