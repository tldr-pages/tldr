# live-server

> A simple development http server with live reload capability.

- Serve an index.html file and reload on changes:

`live-server`

- Specify a port from which to serve a file:

`live-server --port=8081`

- Select file other than index.html to serve: 

`live-server --open=about.html`

- Proxy all requests for ROUTE to URL:

`live-server --proxy=/:http:localhost:3000`
