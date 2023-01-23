# kdocker

> Könnyedén dokkolja az alkalmazásokat a tálcára. További információ: <https://github.com/user-none/KDocker>.

- A kurzor megjelenítése az ablaknak a bal egérgomb megnyomásakor a tálcára küldéséhez (bármely más egérgomb megnyomásával megszakítható):

`kdocker`

- Nyisson meg egy alkalmazást, és küldje azt a tálcára:

`kdocker {{application}}`

- Fókuszált ablak küldése a rendszertálcára:

`kdocker -f`

- A kurzor megjelenítése egy ablaknak a rendszer tálcára küldéséhez egyéni ikonnal a bal egérgomb megnyomásakor:

`kdocker -i {{/path/to/icon}}`

- Egy alkalmazás megnyitása, a rendszertálcára küldése és a fókusz elvesztése esetén minimalizálása:

`kdocker -l {{application}}`

- Nyomtatási verzió:

`kdocker --version`
