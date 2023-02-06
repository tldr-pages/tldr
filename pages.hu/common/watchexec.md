# watchexec

> Tetszőleges parancsok futtatása a fájlok változásakor. További információ: <https://github.com/watchexec/watchexec>.

- A `ls -la` meghívása, amikor az aktuális könyvtárban lévő bármely fájl megváltozik:

`watchexec -- {{ls -la}}`

- A `make` futtatása, amikor az aktuális könyvtárban lévő JavaScript, CSS és HTML fájlok megváltoznak:

`watchexec --exts {{js,css,html}} make`

- A `make` futtatása, ha a `lib` vagy `src` alkönyvtárakban lévő bármely fájl megváltozik:

`watchexec --watch {{lib}} --watch {{src}} {{make}}`

- A `my_server` meghívása/újraindítása, amikor az aktuális könyvtárban lévő bármely fájl megváltozik, a `SIGKILL` elküldése a gyermekfolyamat leállítására:

`watchexec --restart --signal {{SIGKILL}} {{my_server}}`
