# zmap

> Snelle, opensource netwerkscanner voor internetbrede onderzoeken.
> Zie ook: `hping3`, `masscan`, `naabu`, `nmap`, `rustscan`.
> Meer informatie: <https://manned.org/zmap>.

- Scan een subnet of de volledige IPv4-ruimte op een specifieke TCP-poort (standaard: 80):

`sudo zmap {{[-p|--target-ports]}} {{poort}} {{subnet}}`

- Scan specifieke poorten of poortbereiken over een subnet:

`sudo zmap {{[-p|--target-ports]}} {{poort1,poort2-poort3,...}} {{subnet}}`

- Schrijf resultaten weg naar een CSV-bestand met aangepaste velden:

`sudo zmap {{[-o|--output-file]}} {{pad/naar/outputbestand.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{subnet}}`

- Beperk de scansnelheid tot een specifiek aantal pakketten per seconde:

`sudo zmap {{[-r|--rate]}} {{pakketten_per_seconde}} {{subnet}}`

- Simuleer het uitvoeren van zmap zonder pakketten te versturen:

`zmap {{[-d|--dryrun]}} {{subnet}}`

- Sluit subnetten uit met behulp van een blocklistbestand in CIDR-notatie:

`sudo zmap {{[-b|--blocklist-file]}} {{pad/naar/blocklist.txt}} {{subnet}}`

- Stel een specifiek bron-IP in voor scanpakketten:

`sudo zmap {{[-S|--source-ip]}} {{bron_ip}} {{subnet}}`

- Beperk het aantal/percentage doelen om te onderzoeken (bijv. 1000 IP/poort-paren):

`sudo zmap {{[-p|--target-ports]}} {{poort1,poort2-poort3}} {{[-n|--max-targets]}} {{1000}} {{subnet}}`
