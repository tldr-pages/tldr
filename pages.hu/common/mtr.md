# mtr

> Matt's Traceroute: kombinált traceroute és ping eszköz. További információ: <https://bitwizard.nl/mtr>.

- Traceroute egy állomáshoz és folyamatos pingelés minden köztes ugráshoz:

`mtr {{host}}`

- Az IP-cím és az állomásnév leképezésének kikapcsolása:

`mtr -n {{host}}`

- Kimenet generálása minden egyes ugrás 10-szeri pingelése után:

`mtr -w {{host}}`

- IP IPv4 vagy IPV6 kényszerítése:

`mtr -4 {{host}}`

- Várjon egy adott időt (másodpercben), mielőtt újabb csomagot küld ugyanarra a hopra:

`mtr -i {{seconds}} {{host}}`

- Az autonóm rendszer számának (ASN) megjelenítése minden egyes ugráshoz:

`mtr --aslookup {{hostname}}`
