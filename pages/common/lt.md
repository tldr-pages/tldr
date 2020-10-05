# lt

> Localtunnel exposes your localhost to the world for easy testing and sharing! No need to mess with DNS or deploy just to have others test out your changes.
> Great for working with browser testing tools like browserling or external api callback services like twilio which require a public url for callbacks.
> More information: <https://github.com/localtunnel/localtunnel>.

- Start tunnel from a specific port:

`lt --port 8000`

- Specify the upstream server doing the forwarding:

`lt --port 8000 --host {{host}}`

- Request this subdomain:

`lt --port 8000 --subdomain {{subdomain}}`

- Print basic request info:

`lt --port 8000 --print-requests`

- Open the tunnel URL in your browser:

`lt --port 8000 --open`
