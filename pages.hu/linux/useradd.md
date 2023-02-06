# useradd

> Új felhasználó létrehozása. Lásd még: `users`, `userdel`, `usermod`. További információ: <https://manned.org/useradd>.

- Új felhasználó létrehozása:

`sudo useradd {{username}}`

- Új felhasználó létrehozása a megadott felhasználói azonosítóval:

`sudo useradd --uid {{id}} {{username}}`

- Új felhasználó létrehozása a megadott héjjal:

`sudo useradd --shell {{path/to/shell}} {{username}}`

- Új felhasználó létrehozása további csoportokba tartozóként (figyeljen a szóközök hiányára):

`sudo useradd --groups {{group1,group2,...}} {{username}}`

- Új felhasználó létrehozása az alapértelmezett home könyvtárral:

`sudo useradd --create-home {{username}}`

- Új felhasználó létrehozása a sablonkönyvtár-fájlokkal kitöltött házikönyvtárral:

`sudo useradd --skel {{path/to/template_directory}} --create-home {{username}}`

- Új rendszerfelhasználó létrehozása a home könyvtár nélkül:

`sudo useradd --system {{username}}`
