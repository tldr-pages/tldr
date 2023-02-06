# ipset

> A tűzfalszabályok IP-készleteinek létrehozására szolgáló eszköz. További információ: <https://manned.org/ipset>.

- Hozzon létre egy üres IP-készletet, amely IP-címeket tartalmaz:

`ipset create {{set_name}} hash:ip`

- Egy adott IP-készlet megsemmisítése:

`ipset destroy {{set_name}}`

- IP-cím hozzáadása egy adott készlethez:

`ipset add {{set_name}} {{192.168.1.25}}`

- Egy adott IP-cím törlése egy halmazból:

`ipset del {{set_name}} {{192.168.1.25}}`

- IP-készlet mentése:

`ipset save {{set_name}} > {{path/to/ip_set}}`
