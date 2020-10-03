# ack

> Narzędzie wyszukiwania, takie jak grep, zoptymalizowane dla programistów.
> Więcej informacji: <https://beyondgrep.com/documentation/>.

- Znajdź pliki zawierające „foo”:

`ack {{foo}}`

- Znajdź pliki określonego typu:

`ack --ruby {{foo}}`

- Policz całkowitą liczbę dopasowań dla terminu „foo”:

`ack -ch {{foo}}`

- Pokaż nazwy plików zawierające „foo” i liczbę dopasowań w każdym pliku:

`ack -cl {{foo}}`

- Przeszukaj plik pod kątem określonego ciągu znaków:

`ack bar "{{foo bar}}" {{scieżka/do/pliku_lub_katalogu}}`

- Przeszukaj plik pod kątem określonego wzorca regex:

`ack bar "{{[bB]ar \d+}}" {{scieżka/do/pliku_lub_katalogu}}`

- Wypisz wszystkie prawidłowe typy:

`ack --help-types`
