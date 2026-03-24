# openssl rand

> OpenSSL command to generate a random string.
> More information: <https://docs.openssl.org/master/man1/openssl-rand/>.

- Generate hex string:

`openssl rand -hex 8`

- Generate base64 string:

`openssl rand -base64 8`

- Save output to a file:

`openssl rand -hex -out demo.txt 8`
