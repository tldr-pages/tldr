# simplehttpserver

> A simple HTTP/S server that supports file upload, basic authentication, and YAML rules for custom responses.
> A Go alternative to Python's `http.server`.
> More information: <https://github.com/projectdiscovery/simplehttpserver>.

- Start the HTTP server serving the current directory with verbose output (listen on all interfaces and port 8000 by default):

`simplehttpserver -verbose`

- Start the HTTP server with basic authentication serving a specific path over port 80 on all interfaces:

`sudo simplehttpserver -basic-auth {{username}}:{{password}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- Start the HTTP server, enabling HTTPS using a self-signed certificate with custom SAN on all interfaces:

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- Start the HTTP server with custom response headers and upload capability:

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- Start the HTTP server with customizable rules in YAML (see documentation for DSL):

`simplehttpserver -rules {{rules.yaml}}`
