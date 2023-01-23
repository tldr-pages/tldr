# openssl s_client

> OpenSSL parancs TLS ügyfélkapcsolatok létrehozásához. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

- Egy tartomány tanúsítványának kezdő és lejárati dátumának megjelenítése:

`openssl s_client -connect {{host}}:{{port}} 2>/dev/null | openssl x509 -noout -dates`

- Az SSL/TLS-kiszolgáló által bemutatott tanúsítvány megjelenítése:

`openssl s_client -connect {{host}}:{{port}} </dev/null`

- Az SSL/TLS-kiszolgálóhoz való csatlakozáskor a kiszolgálónévjelző (SNI) beállítása:

`openssl s_client -connect {{host}}:{{port}} -servername {{hostname}}`

- Egy HTTPS-kiszolgáló teljes tanúsítványláncának megjelenítése:

`openssl s_client -connect {{host}}:443 -showcerts </dev/null`
