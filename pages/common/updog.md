# updog

> A Replacement for Python's SimpleHTTPServer.
> It allows uploading and downloading via HTTP/S, can set ad hoc SSL certificates and use HTTP basic auth.

- Creates a HTTP server on your current directory:

`updog`

- Creates a HTTP server on a specified directory:

`updog -d /another/directory`

- Creates a HTTP server on a specified port:

`updog -p 1234`

- Creates a HTTP server with a password [To login, you should leave the username blank and just enter the password in the password field]:

`updog --password examplePassword123!`

- Use SSL certificate:

`updog --ssl`
