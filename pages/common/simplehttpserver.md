# simplehttpserver

> A simple HTTP/S server that support file upload, basic auth, and YAML rules for custom responses.
> A Go alternative to Python's http.server.
> More information: <https://github.com/projectdiscovery/simplehttpserver>.

- Start the HTTP server serving the current directory with [v]erbose output (listen on all interfaces and port 8000 by default):

`simplehttpserver -verbose`

- Start the http server with [b]asic auth serving a specific [p]ath over port 80 on all interfaces:

`sudo simplehttpserver -basic-auth {{username}}:{{password}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- Start the http server enabling HTTPS protocol using self-signed certificate with custom SAN on all interfaces:

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- Start the http server with custom response [h]eaders and [u]pload capability:

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- Start the http server with customizable [r]ules in yaml (see documentation for DSL):

`simplehttpserver -rules {{rules.yaml}}`
