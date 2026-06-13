# calibre-server

> Un'applicazione server che può essere usata per distribuire e-book in una rete.
> Gli e-book devono prima essere importati nella libreria usando la GUI o calibredb.
> Parte del manager di e-book Calibre.
> Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Avvia un server per distribuire e-book. Accesso a <http://localhost:8080>:

`calibre-server`

- Avvia il server su una specifica porta. Accesso a <http://localhost:porta>:

`calibre-server --port {{porta}}`

- Proteggi il server con username e password:

`calibre-server --username {{username}} --password {{password}}`
