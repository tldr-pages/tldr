# conntrack

> Interakció a Netfilter kapcsolatkövető rendszerrel. Keresés, listázás, ellenőrzés, módosítás és törlés a kapcsolatfolyamatokban. További információ: <https://manned.org/conntrack>.

- Az összes jelenleg nyomon követett kapcsolat listázása:

`conntrack --dump`

- A kapcsolatváltozások valós idejű eseménynaplójának megjelenítése:

`conntrack --event`

- A kapcsolatváltozások valós idejű eseménynaplójának és a kapcsolódó időbélyegeknek a megjelenítése:

`conntrack --event -o timestamp`

- A kapcsolatváltozások valós idejű eseménynaplójának megjelenítése egy adott IP-címhez:

`conntrack --event --orig-src {{ip_address}}`

- Egy adott forrás IP-címhez tartozó összes adatfolyam törlése:

`conntrack --delete --orig-src {{ip_address}}`
