# openssl rand

> OpenSSL command to generate a random string.
> More information: <https://docs.openssl.org/master/man1/openssl-rand/>.

- Generate a hex string with character length of 8:

`openssl rand -hex 8`

- Generate a base64 string with character length of 20:

`openssl rand -base64 20`

- Save output to a file:

`openssl rand -hex -out {{path/to/output}} {{length}}`
