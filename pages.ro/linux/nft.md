# nft

> Permite configurarea tabelelor, lanţurilor şi regulilor furnizate de firewall-ul kernel-ului Linux.
> Nftables înlocuiește iptables.

- Vizualizaţi configuraţia curentă:

`sudo nft list ruleset`

- Adăugați un tabel nou cu familia „inet” și tabelul „filtru”:

`sudo nft add table {{inet}} {{filter}}`

- Adăugați un nou lanț pentru a accepta tot traficul de intrare:

`sudo nft add chain {{inet}} {{filter}} {{input}} \{ type {{filter}} hook {{input}} priority {{0}} \; policy {{accept}} \}`

- Adăugați o regulă nouă pentru a accepta mai multe porturi TCP:

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- Arată mânerele de reguli:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- Şterge o regulă:

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- Salvați configurația curentă:

`sudo nft list ruleset > {{/etc/nftables.conf}}`
