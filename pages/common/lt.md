# lt

> Localtunnel exposes your localhost to the world for easy testing and sharing.
> More information: <https://github.com/localtunnel/localtunnel>.

- Start tunnel from a specific port:

`lt --port {{8000}}`

- Specify the upstream server doing the forwarding:

`lt --port {{8000}} --host {{host}}`

- Request a specific subdomain:

`lt --port {{8000}} --subdomain {{subdomain}}`

- Print basic request info:

`lt --port {{8000}} --print-requests`

- Open the tunnel URL in the default web browser:

`lt --port {{8000}} --open`
