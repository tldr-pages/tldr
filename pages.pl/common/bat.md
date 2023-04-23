# bat

> Wypisz i łącz pliki.
> Klon `cat` z podświetlaniem składni i integracją z Gitem.
> Więcej informacji: <https://github.com/sharkdp/bat>.

- Wypisz zawartość pliku na standardowe wyjście:

`bat {{ścieżka/do/pliku}}`

- Połącz kilka plików w plik docelowy:

`bat {{plik1}} {{plik2}} > {{plik_docelowy}}`

- Dodaj kilka plików do pliku docelowego:

`bat {{plik1}} {{plik2}} >> {{plik_docelowy}}`

- Ponumeruj wszystkie linie:

`bat --number {{ścieżka/do/pliku}}`

- Podświetl składnię pliku JSON:

`bat --language json {{plik.json}}`

- Wyświetl wszystkie obsługiwane języki:

`bat --list-languages`
