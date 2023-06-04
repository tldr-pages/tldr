# nmap

> Netzwerk erkundungs Werkzeug und Security / Port Scanner.
> Manche Funktionen können nur benutzt werden bei ausführung von Nmap mit root Rechten .
> Weitere Informationen: <https://nmap.org>.

- Überprüfen ob eine IP-Adresse Online ist und Rate das Betriebsystem des remote host's:

`nmap -O {{ip_oder_hostname}}`

- Überprüft nur ob ein Host Online ist (ping Scan):

`nmap -sn {{ip_oder_hostname}} {{optional_noch_eine_addresse}}`

- Scanne zusätzlich nach OS erkennung, version erkennung, traceroute und Scripts:

`nmap -A {{addresse_oder_addressen}}`

- Scanne eine spezifische liste an Ports (benutze '-p-' für alle Ports von 1 bis 65535):

`nmap -p {{port1,port2,...,portN}} {{addresse_oder_addressen}}`

- Führe Dienst und Version Erkennung auf den top 1000 Ports mit dem default NSE Scrips aus; Speicher das Ergebins ('-oN') in der Ausgabe Datei:

`nmap -sC -sV -oN {{Ergebnis.txt}} {{addresse_oder_addressen}}`

- Scanne Ziel(e) vorsichtig mit 'default and safe' NSE Scripts:

`nmap --script "default and safe" {{addresse_oder_addressen}}`

- Scanne einen Wev-Server, der auf den Standart ports 80 und 443 mit allen verfügbaren 'http-*' NSE Scripts:

`nmap --script "http-*" {{addresse_oder_addressen}} -p 80,443`

- Führe einen sehr langsamen verborgenen Scan ('-T0') aus um die Entdeckung von IDS/IPS zu umgehen und benutze Köder IP adressen ('-D'):

`nmap -T0 -D {{köder1_ipaddresse,köder2_ipaddresse,...,köderN_ipaddresse}} {{addresse_oder_addressen}}`
