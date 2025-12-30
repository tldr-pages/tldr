# wcurl

> Prosty wrapper na narzędzie `curl` do łatwego pobierania plików.
> Zobacz także: `wget`, `curl`.
> Więcej informacji: <https://curl.se/wcurl/manual.html>.

- Pobierz zawartość URL do pliku wskazanego przez ten URL (w tym wypadku "index.html"):

`wcurl {{https://example.com/index.html}}`

- Pobierz zawartość URL do pliku o określonej nazwie:

`wcurl {{[-o|--output]}} {{ścieżka/do/pliku}} {{https://example.com/index.html}}`

- Pobierz zawartość URL, wyświetl pasek postępu i domyślnie użyj HTTP/2:

`wcurl --curl-options "--progress-bar --http2" {{https://example.com/index.html}}`

- Wznów przerwane pobieranie:

`wcurl --curl-options "--clobber --continue-at -" {{https://example.com/index.html}}`
