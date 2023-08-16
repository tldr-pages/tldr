# http

> HTTPie: HTTP client, ma być łatwiejszy w użyciu niż cURL.
> Więcej informacji: <https://httpie.org>.

- Pobierz adres URL do pliku:

`http --download {{przyklad.org}}`

- Wyślij dane zakodowane w formularzu:

`http --form {{przyklad.org}} {{nazwa='bob'}} {{zdjecie_profilowe@'bob.png'}}`

- Wyślij obiekt JSON:

`http {{przyklad.org}} {{name='bob'}}`

- Określ metodę HTTP:

`http {{HEAD}} {{przyklad.org}}`

- Dołącz dodatkowy nagłówek:

`http {{przyklad.org}} {{X-MyHeader:123}}`

- Podaj nazwę użytkownika i hasło do uwierzytelnienia serwera:

`http --auth {{nazwauzytkownika:haslo}} {{przyklad.org}}`

- Określ surowe ciało żądania za pośrednictwem `stdin`:

`cat {{dane.txt}} | http PUT {{przyklad.org}}`
