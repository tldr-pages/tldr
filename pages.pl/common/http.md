# http

> HTTPie: klient HTTP przeznaczony do testowania, debugowania i ogólnej interakcji z API i serwerami HTTP.
> Więcej informacji: <https://httpie.io/docs/cli/usage>.

- Wykonaj proste żądanie GET (wyświetla nagłówki odpowiedzi i zawartość):

`http {{https://example.com}}`

- Wyświetl podane części treści (`H`: nagłówki żądania, `B`: treść żądania, `h`: nagłówki odpowiedzi, `b`: treść odpowiedzi, `m`: metadane odpowiedzi):

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- Określ metodę HTTP używaną podczas wysyłania żądania i użyj serwera proxy do przechwycenia żądania:

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- Podążaj za wszystkimi przekierowaniami `3xx` i określ dodatkowe nagłówki do żądania:

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- Uwierzytelnij się na serwerze używając różnych metod uwierzytelniania:

`http {{[-a|--auth]}} {{nazwa_użytkownika:hasło|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- Skonstruuj żądanie, ale go nie wysyłaj:

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- Użyj nazwanych sesji do trwałych niestandardowych nagłówków, danych uwierzytelniających i ciasteczek:

`http --session {{nazwa_sesji|ścieżka/do/sesji.json}} {{[-a|--auth]}} {{nazwa_użytkownika}}:{{hasło}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- Prześlij plik do formularza (poniższy przykład zakłada, że polem formularza jest `<input type="file" name="cv" />`):

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@ścieżka/do/pliku}}`
