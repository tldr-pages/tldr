# gitk

> Grafikus Git tároló böngésző. További információ: <https://git-scm.com/docs/gitk>.

- Az aktuális Git-tárhely böngészőjének megjelenítése:

`gitk`

- Adott fájl vagy könyvtár tárolóhely-böngészőjének megjelenítése:

`gitk {{path/to/file_or_directory}}`

- Az 1 héttel ezelőtti commitok megjelenítése:

`gitk --since="{{1 week ago}}"`

- A 2016. 1/1-nél régebbi commitok megjelenítése:

`gitk --until="{{1/1/2015}}"`

- Legfeljebb 100 változtatás megjelenítése az összes ágban:

`gitk --max-count={{100}} --all`
