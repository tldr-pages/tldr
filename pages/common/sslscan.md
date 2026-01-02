# sslscan

> Check SSL/TLS protocols and ciphers supported by a server.
> More information: <https://manned.org/sslscan>.

- Test a server on port 443:

`sslscan {{example.com}}`

- Test a specified port:

`sslscan {{example.com}}:{{465}}`

- Show certificate information:

`sslscan --show-certificate {{example.com}}`
