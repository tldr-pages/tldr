# nmap

> Tool per esplorazione di rete e scansione porte/sicurezza.
> Alcune funzionalità (es. SYN scan) si attivano solo con privilegi root.
> Vedi anche: `hping3`, `masscan`, `naabu`, `rustscan`, `zmap`.
> Maggiori informazioni: <https://nmap.org/book/man.html>.

- Scansiona le prime 1000 porte di un host remoto con vari livelli di [v]erbosità:

`nmap -v{{1|2|3}} {{ip_o_nome_host}}`

- Esegui ping sweep aggressivo su subnet intera o host individuali:

`nmap -T5 -sn {{192.168.0.0/24|ip_o_nome_host1,ip_o_nome_host2,...}}`

- Abilita rilevamento OS, versione, script scanning e traceroute da file:

`sudo nmap -A -iL {{percorso/del/file.txt}}`

- Scansiona lista specifica di [p]orte (usa `-p-` per tutte le porte da 1 a 65535):

`nmap -p {{porta1,porta2,...}} {{ip_o_host1,ip_o_host2,...}}`

- Rileva servizi e versioni sulle prime 1000 porte con script NSE di default, salva risultati (`-oA`):

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_o_host1,ip_o_host2,...}}`

- Scansiona target con cura usando script NSE `default and safe`:

`nmap --script "default and safe" {{ip_o_host1,ip_o_host2,...}}`

- Scansiona web server su porte standard [p]orte 80 e 443 con tutti gli script `http-*` NSE:

`nmap --script "http-*" {{ip_o_host1,ip_o_host2,...}} -p 80,443`

- Tenta evasione IDS/IPS con scansione lentissima (`-T0`), [D]ecoy indirizzi sorgente, pacchetti [f]rammentati, dati casuali:

`sudo nmap -T0 -D {{decoy_ip1,decoy_ip2,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_o_host}}`
