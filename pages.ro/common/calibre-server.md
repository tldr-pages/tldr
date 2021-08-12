# calibre-server

> O aplicație de server care poate fi utilizată pentru a distribui cărți electronice printr-o rețea.
> Notă: cărțile electronice trebuie deja importate în bibliotecă utilizând GUI sau CLI `calibredb`.
> Mai multe informaţii: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>

- Porniți un server pentru a distribui cărți electronice. Acces la http://localhost:8080:

`calibre-server`

- Porniți serverul pe alt port. Acces la http://localhost:port:

`calibre-server --port {{port}}`

- Parola protejează serverul:

`calibre-server --username {{username}} --password {{password}}`
