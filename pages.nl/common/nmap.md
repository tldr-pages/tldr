# nmap

> Netwerkverkenningstool en beveiligings-/poortscanner.
> Sommige functies (bijv. SYN-scan) worden alleen geactiveerd wanneer `nmap` wordt uitgevoerd met rootprivileges.
> Zie ook: `hping3`, `masscan`, `naabu`, `rustscan`, `zmap`.
> Meer informatie: <https://nmap.org/book/man.html>.

- Scan de top 1000 poorten van een externe host met verschillende [v]erbositeitsniveaus:

`nmap -v{{1|2|3}} {{ip_of_hostnaam}}`

- Voer zeer agressief een ping-sweep uit over een heel [s]ub[n]et of individuele hosts:

`nmap -T5 -sn {{192.168.0.0/24|ip_of_hostnaam1,ip_of_hostnaam2,...}}`

- Schakel OS-detectie, versiedetectie, scriptscanning en traceroute in voor hosts uit een bestand:

`sudo nmap -A -iL {{pad/naar/bestand.txt}}`

- Scan een specifieke lijst van [p]oorten (gebruik `-p-` voor alle poorten van 1 tot 65535):

`nmap -p {{poort1,poort2,...}} {{ip_of_host1,ip_of_host2,...}}`

- Voer service- en versiedetectie uit van de top 1000 poorten met standaard NSE-scripts, en schrijf resultaten (`-oA`) naar outputbestanden:

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_of_host1,ip_of_host2,...}}`

- Scan doelen voorzichtig met de `default and safe` NSE-scripts:

`nmap --script "default and safe" {{ip_of_host1,ip_of_host2,...}}`

- Scan naar webservers die draaien op de standaard[p]oorten 80 en 443 met alle beschikbare `http-*` NSE-scripts:

`nmap --script "http-*" {{ip_of_host1,ip_of_host2,...}} -p 80,443`

- Probeer IDS/IPS-detectie te omzeilen door gebruik te maken van een extreem trage scan (`-T0`), [D]ecoy-bronadressen, [f]ragmentatie van pakketten, willekeurige data en andere methoden:

`sudo nmap -T0 -D {{decoy_ip1,decoy_ip2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_of_host}}`
