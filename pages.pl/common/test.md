# test

> Sprawdza typy plików i porównuje wartości.
> Zwraca 0 gdy porównanie zwróciło wartość poprawną, 1 gdy fałszywą.
> Więcej informacji: <https://www.gnu.org/software/coreutils/test>.

- Sprawdź czy podana zmienna jest równa łańcuchowi znaków:

`test "{{$ZMIENNA}}" == "{{/bin/zsh}}"`

- Sprawdź czy zmienna jest pusta:

`test -z "{{$GIT_BRANCH}}"`

- Sprawdź czy plik istnieje:

`test -f "{{ścieżka/do/pliku}}"`

- Sprawdź czy katalog nie istnieje:

`test ! -d "{{ścieżka/do/katalogu}}"`

- Zapis jeśli porawne-jeśli fałszywe:

`test {{warunek}} && {{echo "gdy poprawne"}} || {{echo "gdy fałszywe"}}`
