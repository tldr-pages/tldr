# iptables

> Program care permite configurarea tabelelor, lanţurilor şi regulilor furnizate de firewall-ul kernel-ului Linux.
> Mai multe informaţii: <https://www.netfilter.org/projects/iptables/>

- Vezi lanțuri, reguli și contoare de pachete/octeți pentru tabelul de filtrare:

`sudo iptables -vnL`

- Setați regula de politică a lanțului:

`sudo iptables -P {{chain}} {{rule}}`

- Adaugă regulă la politica lanțului pentru IP:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Adaugă regulă la politica lanțului pentru IP luând în considerare protocolul și portul:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Şterge regula lanţului:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Salvați configurația iptables a unui tabel dat într-un fișier:

`sudo iptables-save -t {{tablename}} > {{path/to/iptables_file}}`

- Restaurați configurația iptables dintr-un fișier:

`sudo iptables-restore < {{path/to/iptables_file}}`
