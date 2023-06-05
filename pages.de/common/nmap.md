# nmap

> Netzwerk erkundungs Werkzeug und Security / Port Scanner.
> Manche Funktionen können nur benutzt werden bei ausführung von Nmap mit root Rechten.
> Weitere Informationen: <https://nmap.org>.

- Überprüft ob eine IP-Adresse Online ist und Rate das Betriebssystem des remote Host's:

`nmap -O {{ip_oder_hostname}}`

- Überprüft nur ob ein Host Online ist (Ping Scan):

`nmap -sn {{ip_oder_hostname}} {{optional_noch_eine_addresse}}`

- Scanne zusätzlich mit Betriebssystem erkennung, Version erkennung, nach Scripts und nach Traceroute:

`nmap -A {{addresse_oder_addressen}}`

- Scanne eine spezifische Liste an Ports (benutze '-p-' für alle Ports von 1 bis 65535):

`nmap -p {{port1,port2,...,portN}} {{addresse_oder_addressen}}`

- Führe Dienst und Version Erkennung auf den top 1000 Ports mit den Standard NSE Scripts aus; Speicher das Ergebins ('-oN') in der Ausgabe Datei:

`nmap -sC -sV -oN {{ergebnis.txt}} {{addresse_oder_addressen}}`

- Scanne Ziel(e) vorsichtig mit 'default and safe' NSE Scripts:

`nmap --script "default and safe" {{addresse_oder_addressen}}`

- Scanne einen Web-Server, der auf den Standard Ports 80 und 443 mit allen verfügbaren 'http-*' NSE Scripts:

`nmap --script "http-*" {{addresse_oder_addressen}} -p 80,443`

- Führe einen sehr langsamen verborgenen Scan ('-T0') aus um die Entdeckung von IDS/IPS zu umgehen und benutze Köder IP Adressen ('-D'):

`nmap -T0 -D {{köder1_ipaddresse,köder2_ipaddresse,...,köderN_ipaddresse}} {{addresse_oder_addressen}}`
