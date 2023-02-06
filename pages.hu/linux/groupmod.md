# groupmod

> A rendszerben meglévő felhasználói csoportok módosítása. Lásd még: `groups`, `groupadd`, `groupdel`. További információ: <https://manned.org/groupmod>.

- A csoport nevének módosítása:

`sudo groupmod --new-name {{new_group}} {{group_name}}`

- A csoport azonosítójának módosítása:

`sudo groupmod --gid {{new_id}} {{group_name}}`
