# tldr

> Wyświetl proste strony pomocy dla narzędzi wiersza poleceń z projektu tldr-pages.
> Uwaga: opcje `--language` i `--list` nie są wymagane przez specyfikację, ale większość klientów je implementuje.
> Więcej informacji: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Wyświetl stronę tldr dla podanej komendy (wskazówka: w ten sposób tu trafiłeś/aś!):

`tldr {{komenda}}`

- Wyświetl stronę tldr dla podanej podkomendy:

`tldr {{komenda}} {{podkomenda}}`

- Wyświetl stronę tldr dla komendy w podanym języku (jeżeli jest dostępna, w przeciwnym razie po angielsku):

`tldr --language {{kod_języka}} {{komenda}}`

- Wyświetl stronę tldr dla komendy z podanej platformy:

`tldr --platform {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{komenda}}`

- Zaktualizuj lokalną pamięć podręczną stron tldr:

`tldr --update`

- Wyświetl listę stron tldr dla aktualnej platformy i `common`:

`tldr --list`
