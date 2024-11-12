# awk

> Wszechstronny język programowania do pracy na plikach.
> Więcej informacji: <https://github.com/onetrueawk/awk>.

- Wypisz piątą kolumnę (tzw. pole) w pliku oddzielonym spacjami:

`awk '{print $5}' {{ścieżka/do/pliku}}`

- Wypisz drugą kolumnę wierszy zawierających "foo" w pliku oddzielonym spacjami:

`awk '/{{foo}}/ {print $2}' {{ścieżka/do/pliku}}`

- Wypisz ostatnią kolumnę każdego wiersza w pliku, używając przecinka (zamiast spacji) jako separatora pola:

`awk -F ',' '{print $NF}' {{ścieżka/do/pliku}}`

- Zsumuj wartości w pierwszej kolumnie pliku i wypisz łączną wartość:

`awk '{s+=$1} END {print s}' {{ścieżka/do/pliku}}`

- Wypisuj co trzeci wiersz, zaczynając od pierwszego:

`awk 'NR%3==1' {{ścieżka/do/pliku}}`

- Wypisz różne wartości w zależności od warunków:

`awk '{if ($1 == "foo") print "Dokładne dopasowanie foo"; else if ($1 ~ "bar") print "Częściowe dopasowanie bar"; else print "Baz"}' {{ścieżka/do/pliku}}`

- Wypisz wszystkie linie gdzie wartość 10-tej kolumny jest pomiędzy podanymi wartościami:

`awk '($10 >= {{min_wartość}} && $10 <= {{maks_wartość}})'`

- Wypisz tabelę użytkowników z UID >=1000 z nagłówkiem i sformatowanym wyjściem, używając dwukropka jako separatora (`%-20s` oznacza: 20 znaków ciągu wyrównanych do lewej, `%6s` oznacza: 6 znaków ciągu wyrównanych do prawej):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
