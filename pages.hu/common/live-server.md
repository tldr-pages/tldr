# live-server

> Egy egyszerű fejlesztői HTTP-kiszolgáló, amely képes az élő újratöltésre. További információ: <https://github.com/tapio/live-server>.

- Kiszolgál egy `index.html` fájlt és újratöltés a változásokra:

`live-server`

- Adjon meg egy portot (alapértelmezett a 8080), amelyről a fájlt kiszolgálja:

`live-server --port={{8081}}`

- Adja meg a kiszolgálandó fájlt:

`live-server --open={{about.html}}`

- A ROUTE összes kérése az URL címre:

`live-server --proxy={{/}}:{{http:localhost:3000}}`
