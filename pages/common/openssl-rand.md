# openssl rand

> Generate random bytes using a cryptographically secure PRNG.
> More information: <https://docs.openssl.org/master/man1/openssl-rand/>.

- Generate an 8-byte (16 characters) hex string and write it to `stdout`:

`openssl rand -hex 8`

- Generate 20 random bytes encoded in base64:

`openssl rand -base64 20`

- Generate random bytes and write them to a file (without encoding):

`openssl rand -out {{path/to/file}} {{length}}`

- Generate 1 KiB/MiB/GiB/TiB random bytes encoded in hex/base64:

`openssl rand -{{hex|base64}} 1{{K|M|G|T}}`
