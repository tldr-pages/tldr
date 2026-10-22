# updog

> A replacement for Python's SimpleHTTPServer.
> It allows uploading and downloading via HTTP/S, can set ad hoc SSL certificates, and use HTTP basic auth.
> More information: <https://github.com/sc0tfree/updog>.

- Start an HTTP server for the current directory:

`updog`

- Start an HTTP server for a specified directory:

`updog --directory /{{path/to/directory}}`

- Start an HTTP server on a specified port:

`updog --port {{port}}`

- Start an HTTP server with a password (To log in, leave the username blank and enter the password in the password field):

`updog --password {{password}}`

- Enable transport encryption via SSL:

`updog --ssl`
