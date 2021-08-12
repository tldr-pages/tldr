# nmap

> Instrument de explorare a rețelei și scaner de securitate/port.
> Unele caracteristici se activează numai atunci când Nmap este rulat cu privilegii.
> Mai multe informaţii: <https://nmap.org>

- Verificați dacă o adresă IP este în sus și ghiciți sistemul de operare al gazdei de la distanță:

`nmap -O {{ip_or_hostname}}`

- Încercați să determinați dacă gazdele specificate sunt sus și care sunt numele lor:

`nmap -sn {{ip_or_hostname}} {{optional_another_address}}`

- Ca mai sus, dar, de asemenea, executați o scanare TCP implicită de 1000 de porturi dacă gazda pare în sus:

`nmap {{ip_or_hostname}} {{optional_another_address}}`

- De asemenea, activați script-uri, detectarea serviciilor, amprentarea OS și traceroute:

`nmap -A {{address_or_addresses}}`

- Să presupunem o conexiune bună la rețea și să accelereze execuția:

`nmap -T4 {{address_or_addresses}}`

- Scanați o listă specifică de porturi (utilizați „-p-” pentru toate porturile `1-65535”):

`nmap -p {{port1,port2,…,portN}} {{address_or_addresses}}`

- Efectuați scanarea TCP și UDP (utilizați `-su` numai pentru UDP, `-sz` pentru SCTP, `-so` pentru IP):

`nmap -sSU {{address_or_addresses}}`

- Efectuați port complet, serviciu, scanare de detectare a versiunii cu toate scripturile NSE implicite active împotriva unei gazde pentru a determina punctele slabe și informații:

`nmap -sC -sV {{address_or_addresses}}`
