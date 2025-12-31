# calibre-server

> A server application to distribute e-books over a network.
> Note: E-books must already be imported into the library using the GUI or the `calibredb` CLI.
> Part of the Calibre e-book library.
> More information: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Start a server to distribute e-books. Access at <http://localhost:8080>:

`calibre-server`

- Start server on different port. Access at <http://localhost:port>:

`calibre-server --port {{port}}`

- Password protect the server:

`calibre-server --username {{username}} --password {{password}}`
