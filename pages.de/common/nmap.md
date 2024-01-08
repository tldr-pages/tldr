# nmap

> Netzwerk-Erkundungs-Werkzeug und Security / Port Scanner.
> Manche Funktionen können nur benutzt werden, wenn Nmap mit Root Rechten ausgeführt wird.
> Weitere Informationen: <https://nmap.org>.

- Überprüfe ob eine IP-Adresse online ist und versuche, das Betriebssystem herauszufinden:

`nmap -O {{ip_oder_hostname}}`

- Überprüfe nur ob die angegebenen Hosts online sind (Ping Scan) und ihre Domain-Namen:

`sudo nmap -sn {{ip_oder_hostname}} {{optional_noch_eine_addresse}}`

- Scanne zusätzlich mit Skripten, Service-Erkennung, Betriebssystem-Fingerprinting und Traceroute:

`nmap -A {{addresse_oder_addressen}}`

- Scanne eine spezifische Liste an Ports (benutze '-p-' für alle Ports von 1 bis 65535):

`nmap -p {{port1,port2,...,portN}} {{addresse_oder_addressen}}`

- Führe Dienst- und Versions-Erkennung auf den top 1000 Ports mit den Standard NSE Skripten aus; und schreibe das Ergebnis ('-oN') in der Ausgabe Datei:

`nmap -sC -sV -oN {{ergebnis.txt}} {{addresse_oder_addressen}}`

- Scanne Ziel(e) vorsichtig mit 'default and safe' NSE Scripts:

`nmap --script "default and safe" {{addresse_oder_addressen}}`

- Scanne einen Web-Server, der auf den Standard Ports 80 und 443 läuft, mit allen verfügbaren 'http-*' NSE Skripten:

`nmap --script "http-*" {{addresse_oder_addressen}} -p 80,443`

- Führe einen sehr langsamen verborgenen Scan ('-T0') aus um die Entdeckung von IDS/IPS zu umgehen und benutze Köder IP-Adressen ('-D'):

`nmap -T0 -D {{köder1_ipaddresse,köder2_ipaddresse,...,köderN_ipaddresse}} {{addresse_oder_addressen}}`
