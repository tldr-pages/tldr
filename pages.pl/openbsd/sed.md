# sed

> Edytuj tekst w sposób skryptowalny.
> Zobacz także: `awk`, `ed`.
> Więcej informacji: <https://man.openbsd.org/sed.1>.

- Zastąp wszystkie wystąpienia `jabłko` (podstawowe wyrażenie regularne) przez `mango` (podstawowe wyrażenie regularne) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

`{{komenda}} | sed 's/jabłko/mango/g'`

- Wykonaj określony plik (z ang. [f]ile) skryptu i wypisz jego wynik do `stdout`:

`{{komenda}} | sed -f {{ścieżka/do/skryptu.sed}}`

- Opóźnij otwarcie każdego pliku do momentu, gdy polecenie zawierające powiązaną funkcję lub flagę `w` zostanie zastosowane do linii wejścia:

`{{komenda}} | sed -fa {{ścieżka/do/skryptu.sed}}`

- Zastąp wszystkie wystąpienia `jabłko` (rozszerzone wyrażenie regularne) przez `JABŁKO` (rozszerzone wyrażenie regularne) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

`{{komenda}} | sed -E 's/(jabłko)/\U\1/g'`

- Wypisz tylko pierwszą linię do `stdout`:

`{{komenda}} | sed -n '1p'`

- Zastąp wszystkie wystąpienia `jabłko` (podstawowe wyrażenie regularne) przez `mango` (podstawowe wyrażenie regularne) w określonym pliku i nadpisz oryginalny plik:

`sed -i 's/jabłko/mango/g' {{ścieżka/do/pliku}}`
