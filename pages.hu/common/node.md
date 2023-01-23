# node

> Szerveroldali JavaScript platform (Node.js). További információ: <https://nodejs.org>.

- Egy JavaScript fájl futtatása:

`node {{path/to/file}}`

- Indítson el egy REPL-t (interaktív héj):

`node`

- A megadott fájl végrehajtása, a folyamat újraindítása az importált fájl módosításakor (Node.js 18.11+ verzió szükséges):

`node --watch {{path/to/file}}`

- JavaScript kód kiértékelése a kód argumentumként történő átadásával:

`node -e "{{code}}"`

- Kiértékelés és az eredmény kiírása, hasznos a node függőségi verziók megtekintéséhez:

`node -p "{{process.versions}}"`

- Az ellenőr aktiválása, a végrehajtás szüneteltetése a debugger csatlakoztatásáig, amint a forráskód teljes mértékben elemezve van:

`node --no-lazy --inspect-brk {{path/to/file}}`
