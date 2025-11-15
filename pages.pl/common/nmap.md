# nmap

> Narzędzie do eksploracji sieci oraz skaner bezpieczeństwa/portów.
> Niektóre funkcje (np. skan SYN) aktywują się tylko gdy `nmap` jest uruchamiany z przywilejami root'a.
> Więcej informacji: <https://nmap.org/book/man.html>.

- Skanuj 1000 najpopularniejszych portów zdalnego hosta z różnymi poziomami szczegółowości ([v]erbosity):

`nmap -v{{1|2|3}} {{ip_lub_nazwa_hosta}}`

- Wykonaj bardzo agresywnie ping sweep w całej podsieci lub na poszczególnych hostach:

`nmap -T5 -sn {{192.168.0.0/24|ip_lub_nazwa_hosta1,ip_lub_nazwa_hosta2,...}}`

- Włącz wykrywanie systemu operacyjnego, wykrywanie wersji, skanowanie skryptów i traceroute hostów z pliku:

`sudo nmap -A -iL {{ścieżka/do/pliku.txt}}`

- Skanuj podaną listę portów (użyj `-p-` dla wszystkich portów od 1 do 65535):

`nmap -p {{port1,port2,...}} {{ip_lub_host1,ip_lub_host2,...}}`

- Przeprowadź wykrywanie usług i wersji dla 1000 najpopularniejszych portów używając domyślnych skryptów NSE, zapisując wynik (`-oA`) do plików wyjściowych:

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_lub_host1,ip_lub_host2,...}}`

- Skanuj cel(e) ostrożnie używając skryptów NSE `default and safe`:

`nmap --script "default and safe" {{ip_lub_host1,ip_lub_host2,...}}`

- Skanuj w poszukiwaniu serwerów internetowych działających na standardowych portach 80 i 443 przy użyciu wszystkich dostępnych skryptów NSE `http-*`:

`nmap --script "http-*" {{ip_lub_host1,ip_lub_host2,...}} -p 80,443`

- Spróbuj uniknąć wykrycia przez IDS/IPS, używając bardzo powolnego skanowania (`-T0`), fałszywych adresów źródłowych - wabików (`-D`), [f]ragmentowanych pakietów, losowych danych i innych metod:

`sudo nmap -T0 -D {{ip_wabika1,ip_wabika2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_lub_host}}`
