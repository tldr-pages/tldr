# masscan

> Bardzo efektywny skaner sieci.
> Najlepiej używać z podwyższonymi uprawnieniami. Żeby sprawdzić kompatybilność z Nmap'em, użyj komendy `masscan --nmap`.
> Więcej informacji: <https://github.com/robertdavidgraham/masscan>.

- Skanuj adres IP lub podsieć w poszukowaniu portu 80:

`masscan {{adres_ip|maska_podsieci}} --ports {{80}}`

- Skanuj podsieć klasy B w dla 100 najwyższych portów z prędkością 100,000 pakietów na sekundę:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- Skanuj podsieć klasy B unikając zakresów adresów zadanych z pliku:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{ścieżka/do/pliku}}`

- Skanuj Internet w poszukowaniu portu 443:

`masscan {{0.0.0.0/0}} --ports {{443}} --rate {{10000000}}`

- Skanuj Internet dla zadanego zakresu portów i eksportuj wynik do pliku:

`masscan {{0.0.0.0/0}} --ports {{0-65535}} -output-format {{binary|grepable|json|list|xml}} --output-filename {{ścieżka/do/pliku}}`
