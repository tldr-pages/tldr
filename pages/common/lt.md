# lt

> localtunnel exposes your localhost to the world for easy testing and sharing! No need to mess with DNS or deploy just to have others test out your changes.
> Great for working with browser testing tools like browserling or external api callback services like twilio which require a public url for callbacks.
> More information: <https://github.com/localtunnel/localtunnel>.

- Start tunnel in a specific port:

`lt -p 8000`

- Upstream server providing forwarding:

`lt --port 8000 -h {{host}}`

- Request this subdomain:

`lt --port 8000 -s {{subdomain}}`

- Print basic request info:

`lt --port 8000 --print-requests`

- Opens the tunnel URL in your browser:

`lt --port 8000 -o`
