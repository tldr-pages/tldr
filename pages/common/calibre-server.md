# calibre-server

> A server application that can be used to distribute ebooks over a network.
> Ebooks must be imported into the library using the GUI or calibredb before.
> Part of the Calibre ebook library.
> More information: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Start a server to distribute ebooks. Access at http://localhost:8080:

`calibre-server`

- Start server on different port. Access at http://localhost:port:

`calibre-server --port {{port}}`

- Password protect the server:

`calibre-server --username {{username}} --password {{password}}`
