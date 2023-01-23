# sv

> Egy futó runsv szolgáltatás vezérlése. További információ: <https://manpages.ubuntu.com/manpages/latest/man8/sv.8.html>.

- Egy szolgáltatás indítása:

`sudo sv up {{path/to/service}}`

- Egy szolgáltatás leállítása:

`sudo sv down {{path/to/service}}`

- A szolgáltatás állapotának lekérdezése:

`sudo sv status {{path/to/service}}`

- Egy szolgáltatás újratöltése:

`sudo sv reload {{path/to/service}}`

- Indítson el egy szolgáltatást, de csak akkor, ha az nem fut, és ne indítsa újra, ha leáll:

`sudo sv once {{path/to/service}}`
