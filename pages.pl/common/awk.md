# awk

> Wszechstronny język programowania do pracy na plikach.
> Więcej informacji: <https://github.com/onetrueawk/awk>.

- Wydrukuj piątą kolumnę (aka. pole) w pliku oddzielonym spacjami:

`awk '{print $5}' {{nazwapliku}}`

- Wydrukuj drugą kolumnę wierszy zawierających "something" w pliku oddzielonym spacjami:

`awk '/{{coś}}/ {print $2}' {{nazwapliku}}`

- Wydrukuj ostatnią kolumnę każdego wiersza w pliku, używając przecinka (zamiast spacji) jako separatora pola:

`awk -F ',' '{print $NF}' {{nazwapliku}}`

- Zsumuj wartości w pierwszej kolumnie pliku i wydrukuj sumę:

`awk '{s+=$1} END {print s}' {{nazwapliku}}`

- Drukuj co trzeci wiersz, zaczynając od pierwszego wiersza:

`awk 'NR%3==1' {{nazwapliku}}`

- Wydrukuj różne wartości w zależności od warunków:

`awk '{if ($1 == "foo") print "Dokładne dopasowanie foo"; else if ($1 ~ "bar") print "Częściowe dopasowanie bar"; else print "Baz"}' {{nazwapliku}}`

- Wydrukuj wszystkie linie gdzie wartość 10-tej kolumny jest równa podanej wartości:

`awk '($10 == {{wartość}})'`

- Wydrukuj wszystkie linie, w których wartość 10-tej kolumny jest pomiędzy podanymi wartościami:

`awk '($10 >= {{wartość_minimalna}} && $10 <= {{wartość_maksymalna}})'`
