# httping

> Measure the latency and throughput of a web server.
> More information: <https://manned.org/httping>.

- Ping the specified URL:

`httping -g {{url}}`

- Ping the web server on `host` and `port`:

`httping -h {{host}} -p {{port}}`

- Ping the web server on `host` using a TLS connection:

`httping -l -g https://{{host}}`

- Ping the web server on `host` using HTTP basic authentication:

`httping -g http://{{host}} -U {{username}} -P {{password}}`
