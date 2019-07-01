# calibre-server

> Un'applicazione server che può essere usata per distribuire ebook in una rete.
> Gli ebook devono prima essere importati nella libreria usando la GUI o calibredb.
> Parte del manager di ebook Calibre.
> Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Avvia un server per distribuire ebook. Accesso a http://localhost:8080:

`calibre-server`

- Avvia il server su una specifica porta. Accesso a http://localhost:porta:

`calibre-server --port {{porta}}`

- Proteggi il server con username e password:

`calibre-server --username {{username}} --password {{password}}`
