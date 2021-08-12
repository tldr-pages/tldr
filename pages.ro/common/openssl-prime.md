# openssl prime

> comanda OpenSSL pentru a calcula numerele prime.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>

- Generați un număr prim de 2048bit și afișați-l în hexazecimal:

`openssl prime -generate -bits 2048 -hex`

- Verificați dacă un număr dat este prim:

`openssl prime {{number}}`
