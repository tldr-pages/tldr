# updog

> A Replacement for Python's SimpleHTTPServer.
> It allows uploading and downloading via HTTP/S, can set ad hoc SSL certificates and use HTTP basic auth.
> More information: <https://github.com/sc0tfree/updog>.

- Start a HTTP server on your current directory:

`updog`

- Start a HTTP server on a specified directory:

`updog --directory {{/path/to/directory}}`

- Start a HTTP server on a specified port:

`updog --port {{port}}`

- Start a HTTP server with a password [To login, you should leave the username blank and just enter the password in the password field]:

`updog --password {{password}}`

- Use SSL certificate:

`updog --ssl`
