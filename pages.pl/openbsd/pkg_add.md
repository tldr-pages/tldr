# pkg_add

> Instaluj/aktualizuj pakiety w OpenBSD.
> Zobacz także: `pkg_info`, `pkg_delete`.
> Więcej informacji: <https://man.openbsd.org/pkg_add>.

- Zaktualizuj wszystkie pakiety, w tym zależności:

`pkg_add -u`

- Zainstaluj nowy pakiet:

`pkg_add {{pakiet}}`

- Zainstaluj pakiety z surowego wyjścia `pkg_info`:

`pkg_add -l {{ścieżka/do/pliku}}`
