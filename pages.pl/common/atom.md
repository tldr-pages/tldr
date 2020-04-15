# atom

> Wieloplatformowy edytor tekstu z możliwością wtyczek.
> Wtyczkami zarządza się poprzez `apm`.
> Więcej informacji: <https://atom.io/>.

- Otwórz plik lub katalog:

`atom {{path/to/file_or_directory}}`

- Otwórz plik lub katalog w nowym oknie:

`atom -n {{path/to/file_or_directory}}`

- Otwórz plik lub katalog w istniejącym oknie:

`atom --add {{path/to/file_or_directory}}`

- Otwórz Atom w trybie bezpieczeństwa (nie ładuje żadnych dodatkowych pakietów):

`atom --safe`

- Zapobiegaj atomowi rozwidlania się w tle, utrzymując Atom podłączony do terminala:

`atom --foreground`

- Poczekaj na zamknięcie okna Atom przed powrotem (przydatne dla git commit editor):

`atom --wait`
