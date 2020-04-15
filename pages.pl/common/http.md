# http

> HTTPie: HTTP client, ma być łatwiejszy w użyciu niż cURL.
> Więcej informacji: <https://httpie.org>.

- Pobierz adres URL do pliku:

`http -d {{example.org}}`

- Wyślij dane zakodowane w formularzu:

`http -f {{example.org}} {{name='bob'}} {{profile_picture@'bob.png'}}`

- Wyślij obiekt JSON:

`http {{example.org}} {{name='bob'}}`

- Określ metodę HTTP:

`http {{HEAD}} {{example.org}}`

- Dołącz dodatkowy nagłówek:

`http {{example.org}} {{X-MyHeader:123}}`

- Podaj nazwę użytkownika i hasło do uwierzytelnienia serwera:

`http -a {{username:password}} {{example.org}}`

- Określ surowe ciało żądania za pośrednictwem `stdin`:

`cat {{data.txt}} | http PUT {{example.org}}`
