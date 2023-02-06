# a2query

> Az Apache futásidejű konfigurációjának lekérése Debian-alapú operációs rendszereken. További információ: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Engedélyezett Apache modulok listája:

`sudo a2query -m`

- Ellenőrizze, hogy egy adott modul telepítve van-e:

`sudo a2query -m {{module_name}}`

- Engedélyezett virtuális hosztok listája:

`sudo a2query -s`

- Az aktuálisan engedélyezett több feldolgozó modul megjelenítése:

`sudo a2query -M`

- Az Apache verziójának megjelenítése:

`sudo a2query -v`
