# hping3

> Fejlett ping segédprogram, amely támogatja az olyan protokollokat, mint a TCP, UDP és nyers IP. Legjobb, ha emelt jogosultságokkal futtatod. További információ: <https://github.com/antirez/hping>.

- Egy célállomás pingelése 4 ICMP ping-kéréssel:

`hping3 --icmp --count {{4}} {{ip_or_hostname}}`

- A 80-as TCP-port vizsgálatát, az 5090-es adott helyi forrásportról történő vizsgálatot:

`hping3 --verbose --syn --destport {{80}} --baseport {{5090}} {{ip_or_hostname}}`

- Traceroute egy adott célportra irányuló TCP-ellenőrzéssel:

`hping3 --traceroute --verbose --syn --destport {{80}} {{ip_or_hostname}}`

- TCP ACK letapogatás végrehajtása annak ellenőrzésére, hogy egy adott állomás él-e:

`hping3 --count {{2}} --verbose --destport {{80}} -A {{ip_or_hostname}}`
