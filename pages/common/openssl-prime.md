# openssl prime

> OpenSSL command to compute prime numbers.
> More information: <https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>.

- Generate a 2048bit prime number in hexadecimal format:

`openssl prime -generate -bits 2048 -hex`

- Check if given number is prime:

`openssl prime {{number}}`
