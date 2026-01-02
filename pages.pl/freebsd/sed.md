# sed

> Edytuj tekst w sposób skryptowalny.
> Zobacz także: `awk`, `ed`.
> Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?sed>.

- Zamień wszystkie wystąpienia `jabłko` (podstawowe `regex`) na `mango` (podstawowe `regex`) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

`{{komenda}} | sed 's/jabłko/mango/g'`

- Uruchom określony plik (z ang. [f]ile) skryptu i wydrukuj wynik na `stdout`:

`{{komenda}} | sed -f {{ścieżka/do/skryptu.sed}}`

- Opóźnij otwieranie każdego pliku, dopóki polecenie zawierające powiązaną funkcję lub flagę `w` nie zostanie zastosowane do linii wejściowej:

`{{komenda}} | sed -fa {{ścieżka/do/skryptu.sed}}`

- Zamień wszystkie wystąpienia `jabłko` (rozszerzone `regex`) na `JABŁKO` (rozszerzone `regex`) we wszystkich liniach wejściowych i wypisz wynik do `stdout`:

`{{komenda}} | sed -E 's/(jabłko)/\U\1/g'`

- Wypisz tylko pierwszą linię do `stdout`:

`{{komenda}} | sed -n '1p'`

- Zamień wszystkie wystąpienia `jabłko` (podstawowe `regex`) na `mango` (podstawowe `regex`) w określonym pliku i nadpisz oryginalny plik:

`sed -i 's/jabłko/mango/g' {{ścieżka/do/skryptu}}`
