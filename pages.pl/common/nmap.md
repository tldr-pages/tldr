# nmap

> Narzędzie do enumeracji sieci oraz skanowania portów.
> Niektóre funkcję są tylko aktywne gdy Nmap uruchamiany jest z przywilejami root'a.
> Więcej informacji: <https://nmap.org>.

- Sprawdź czy host odpowiada na skanowanie oraz zgadnij system operacyjny:

`nmap -O {{ip_lub_nazwa_hosta}}`

- Sprawdź czy podane hosty odpowiadają na skanowanie i zgadnij ich nazwy:

`nmap -sn {{ip_lub_nazwa_hosta}} {{opcjonalny_kolejny_adres_ip}}`

- Poza tym, uruchom domyśle skrypty, wykrywanie działających serwisów, OS fingerprinting oraz komendę traceroute:

`nmap -A {{adres_lub_adresy_ip}}`

- Skanuj podaną listę portów (użyj '-p-' dla wszystkich portów od 1 do 65535):

`nmap -p {{port1,port2,...,portN}} {{adres_lub_adresy_ip}}`

- Przeprowadź wykrywanie serwisów i ich wersji dla 1000 najczęstrzych portów używając domyślich skryptów NSE; Zapisz rezultat ('-oN') do pliku wyjściowego:

`nmap -sC -sV -oN {{top-1000-ports.txt}} {{adres_lub_adresy_ip}}`

- Skanuj cel lub cele używając skryptów NSE 'default and safe':

`nmap --script "default and safe" {{adres_lub_adresy_ip}}`

- Skanuj serwer webowy uruchomiony na standardowych portach 80 i 443 używając wszystkich dostępnych skryptów NSE 'http-*':

`nmap --script "http-*" {{adres_lub_adresy_ip}} -p 80,443`

- Wykonaj skryty i bardzo wolny skan ('-T0') próbując uniknąć wykrycia przez IDS/IPS i użyj adresu IP wabika ('-D'):

`nmap -T0 -D {{adres_ip_wabika1,adres_ip_wabika2,...,adres_ip_wabikaN}} {{adres_lub_adresy_ip}}`
