# openssl s_client

> comanda OpenSSL pentru a crea conexiuni client TLS.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>

- Afișează datele de început și de expirare pentru certificatul unui domeniu:

`openssl s_client -connect {{host}}:{{port}} 2>/dev/null | openssl x509 -noout -dates`

- Afișează certificatul prezentat de un server SSL/TLS:

`openssl s_client -connect {{host}}:{{port}} </dev/null`

- Afișează lanțul complet de certificate al unui server HTTPS:

`openssl s_client -connect {{host}}:443 -showcerts </dev/null`
