# http

> HTTPie: HTTP kliens, célja, hogy könnyebben használható legyen, mint a cURL. További információ [: https://httpie.org](https://httpie.org).

- URL letöltése egy fájlba:

`http --download {{example.org}}`

- Formanyomtatványon kódolt adatok küldése:

`http --form {{example.org}} {{name='bob'}} {{profile_picture@'bob.png'}}`

- JSON objektum küldése:

`http {{example.org}} {{name='bob'}}`

- HTTP-módszer megadása:

`http {{HEAD}} {{example.org}}`

- Extra fejléc felvétele:

`http {{example.org}} {{X-MyHeader:123}}`

- Felhasználónév és jelszó átadása a kiszolgáló hitelesítéséhez:

`http --auth {{username:password}} {{example.org}}`

- A kérés nyers testének megadása a `stdin` címen keresztül:

`cat {{data.txt}} | http PUT {{example.org}}`
