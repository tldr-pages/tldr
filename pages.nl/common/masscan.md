# masscan

> Een zeer snelle netwerkscanner.
> Werkt het beste met verhoogde privileges. Voor hulp met Nmap-compatibiliteit, voer `masscan --nmap` uit.
> Zie ook: `hping3`, `naabu`, `nmap`, `rustscan`, `zmap`.
> Meer informatie: <https://manned.org/masscan>.

- Scan een IP of netwerksubnet op poort 80:

`masscan {{ip_adres|netwerk_prefix}} {{[-p|--ports]}} {{80}}`

- Scan een klasse B-subnet op de top 100 poorten met 100.000 pakketten per seconde:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- Scan een klasse B-subnet en vermijd bereiken uit een specifiek uitsluitingsbestand:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{pad/naar/bestand}}`

- Scan een klasse B-subnet met Nmap-achtige versiedetectie (banner grabbing):

`masscan {{10.0.0.0/16}} {{[-p|--ports]}} {{22,80}} --banners --rate {{100000}}`

- Scan het internet op webservers die draaien op poort 80 en 443:

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{80,443}} --rate {{10000000}}`

- Scan het internet op DNS-servers die draaien op UDP-poort 53:

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{U:53}} --rate {{10000000}}`

- Scan het internet op een specifiek poortbereik en exporteer naar een bestand:

`masscan {{0.0.0.0/0}} {{[-p|--ports]}} {{0-65535}} --output-format {{binary|grepable|json|list|xml}} --output-filename {{pad/naar/bestand}}`

- Lees binaire scanresultaten uit een bestand en geef ze weer op `stdout`:

`masscan --readscan {{pad/naar/bestand}}`
