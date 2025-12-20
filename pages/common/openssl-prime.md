# openssl prime

> OpenSSL command to compute prime numbers.
> More information: <https://docs.openssl.org/master/man1/openssl-prime/>.

- Generate a 2048bit prime number and display it in hexadecimal:

`openssl prime -generate -bits 2048 -hex`

- Check if a given number is prime:

`openssl prime {{number}}`
