# sed

> Edycja tekstu w sposób skryptowalny.
> Zobacz także: `awk`, `ed`.
> Więcej informacji: <https://man.openbsd.org/sed.1>.

- Zastąp wszystkie wystąpienia `jablko` (podstawowe wyrażenie regularne) przez `mango` (podstawowe wyrażenie regularne) we wszystkich liniach wejściowych i wypisuje wynik do `stdout`:

`{{komenda}} | sed 's/jablko/mango/g'`

- Wykonuje określony plik (z ang. [f]ile) skryptu i wypisuje wynik do `stdout`:

`{{komenda}} | sed -f {{sciezka/do/skryptu.sed}}`

- Opóźnia otwarcie każdego pliku do momentu, gdy polecenie zawierające powiązaną funkcję lub flagę `w` zostanie zastosowane do linii wejścia:

`{{komenda}} | sed -fa {{sciezka/do/skryptu.sed}}`

- Zastąp wszystkie wystąpienia `jablko` (rozszerzone wyrażenie regularne) przez `JABLKO` (rozszerzone wyrażenie regularne) we wszystkich liniach wejściowych i wypisuje wynik do `stdout`:

`{{komenda}} | sed -E 's/(jablko)/\U\1/g'`

- Wypisz tylko pierwszą linię do `stdout`:

`{{komenda}} | sed -n '1p'`

- Zastąp wszystkie wystąpienia `jablko` (podstawowe wyrażenie regularne) przez `mango` (podstawowe wyrażenie regularne) w określonym pliku i nadpisuje oryginalny plik:

`sed -i 's/jablko/mango/g' {{sciezka/do/pliku}}`
