# groupadd

> Felhasználói csoportok hozzáadása a rendszerhez. Lásd még: `groups`, `groupdel`, `groupmod`. További információ: <https://manned.org/groupadd>.

- Új csoport létrehozása:

`sudo groupadd {{group_name}}`

- Új rendszercsoport létrehozása:

`sudo groupadd --system {{group_name}}`

- Új csoport létrehozása az adott groupiddel:

`sudo groupadd --gid {{id}} {{group_name}}`
