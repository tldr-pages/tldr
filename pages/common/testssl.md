# testssl

> Check SSL/TLS protocols and ciphers supported by a server.
> More information: <https://testssl.sh/>.

- Test a server (run every check) on port 443:

`testssl {{example.com}}`

- Test a different port:

`testssl {{example.com:465}}`

- Only check available protocols:

`testssl --protocols {{example.com}}`

- Only check vulnerabilities:

`testssl --vulnerable {{example.com}}`

- Only check HTTP security headers:

`testssl --headers {{example.com}}`
