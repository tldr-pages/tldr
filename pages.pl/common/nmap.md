# nmap

> Narzędzie do enumeracji sieci oraz skanowania portów.
> Niektóre funkcję są tylko aktywne gdy Nmap uruchamiany jest z przywilejami root'a.
> Więcej informacji: <https://nmap.org>.

- Sprawdź czy host odpowiada na skanowanie oraz zgadnij system operacyjny:

`nmap -O {{ip_or_hostname}}`

- Sprawdź czy podane hosty odpowiadają na skanowanie i zgadnij ich nazwy:

`nmap -sn {{ip_or_hostname}} {{optional_another_address}}`

- Poza tym, uruchom domyśle skrypty, wykrywanie działających serwisów, OS fingerprinting oraz komendę traceroute:

`nmap -A {{address_or_addresses}}`

- Skanuj podaną listę portów (użyj '-p-' dla wszystkich portów od 1 do 65535):

`nmap -p {{port1,port2,...,portN}} {{address_or_addresses}}`

- Przeprowadź wykrywanie serwisów i ich wersji dla 1000 najczęstrzych portów używając domyślich skryptów NSE; Zapisz rezultat ('-oN') do pliku wyjściowego:

`nmap -sC -sV -oN {{top-1000-ports.txt}} {{address_or_addresses}}`

- Skanuj cel lub cele używając skryptów NSE 'default and safe':

`nmap --script "default and safe" {{address_or_addresses}}`

- Skanuj serwer webowy uruchomiony na standardowych portach 80 i 443 używając wszystkich dostępnych skryptów NSE 'http-*':

`nmap --script "http-*" {{address_or_addresses}} -p 80,443`

- Wykonaj skryty i bardzo wolny skan ('-T0') próbując uniknąć wykrycia przez IDS/IPS i użyj adresu IP wabika ('-D'):

`nmap -T0 -D {{decoy1_ipaddress,decoy2_ipaddress,...,decoyN_ipaddress}} {{address_or_addresses}}`
