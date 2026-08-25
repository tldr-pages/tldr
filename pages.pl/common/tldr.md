# tldr

> Wyświetl proste strony pomocy dla narzędzi wiersza poleceń z projektu tldr-pages.
> Uwaga: opcje `--language` i `--list` nie są wymagane przez specyfikację, ale większość klientów je implementuje.
> Więcej informacji: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Wyświetl stronę tldr dla podanej komendy (wskazówka: w ten sposób tu trafiłeś/aś!):

`tldr {{komenda}}`

- Wyświetl stronę tldr dla podanej podkomendy:

`tldr {{komenda}} {{podkomenda}}`

- Wyświetl stronę tldr dla komendy w podanym języku (jeżeli jest dostępna, w przeciwnym razie po angielsku):

`tldr {{[-L|--language]}} {{kod_języka}} {{komenda}}`

- Wyświetl stronę tldr dla komendy z podanej platformy:

`tldr {{[-p|--platform]}} {{android|cisco-ios|common|dos|freebsd|linux|netbsd|openbsd|osx|sunos|windows}} {{komenda}}`

- Zaktualizuj lokalną pamięć podręczną stron tldr:

`tldr {{[-u|--update]}}`

- Wyświetl listę stron tldr dla aktualnej platformy i `common`:

`tldr {{[-l|--list]}}`

- Przeglądaj strony tldr w oknie terminala (`fzf` musi być zainstalowany):

`tldr {{[-l|--list]}} | fzf --preview "tldr {1} --color=always" --preview-window=right,70% | xargs tldr`

- Wyświetl stronę tldr dla losowej komendy:

`tldr {{[-l|--list]}} | shuf {{[-n|--head-count]}} 1 | xargs tldr`
