# mdutil

> A Spotlight által indexeléshez használt metaadattárolók kezelése. További információ: <https://ss64.com/osx/mdutil.html>.

- Az indító kötet indexelési állapotának megjelenítése:

`mdutil -s {{/}}`

- A Spotlight indexelés be- és kikapcsolása egy adott kötet esetében:

`mdutil -i {{on|off}} {{path/to/volume}}`

- Az összes kötet indexelésének be/ki kapcsolása:

`mdutil -a -i {{on|off}}`

- A metaadattárolók törlése és az indexelési folyamat újraindítása:

`mdutil -E {{path/to/volume}}`
