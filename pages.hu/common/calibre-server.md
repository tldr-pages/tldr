# calibre-server

> Kiszolgáló alkalmazás, amely e-könyvek hálózaton keresztüli terjesztésére használható. Megjegyzés: az e-könyveket már be kell importálni a könyvtárba a GUI vagy a `calibredb` CLI segítségével. További információ: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Indítson el egy kiszolgálót e-könyvek terjesztéséhez. Hozzáférés a http://localhost:8080 címen:

`calibre-server`

- Kiszolgáló indítása más porton. Hozzáférés a http://localhost:port címen:

`calibre-server --port {{port}}`

- Jelszóval védje a szervert:

`calibre-server --username {{username}} --password {{password}}`
