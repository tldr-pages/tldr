# iptables

> A Linux kernel tűzfal által biztosított táblázatok, láncok és szabályok konfigurálását lehetővé tevő program. További információ: <https://www.netfilter.org/projects/iptables/>.

- A szűrőtábla láncainak, szabályainak és csomag-/byte-számlálóinak megtekintése:

`sudo iptables -vnL`

- Láncpolitikai szabály beállítása:

`sudo iptables -P {{chain}} {{rule}}`

- Szabály hozzáadása a láncpolitikához az IP-hez:

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Szabály hozzáadása az IP protokollt és portot figyelembe vevő láncházirendhez:

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- NAT-szabály hozzáadása a `192.168.0.0/24` alhálózatból érkező összes forgalom lefordításához az állomás nyilvános IP-címére:

`sudo iptables -t {{nat}} -A {{POSTROUTING}} -s {{192.168.0.0/24}} -j {{MASQUERADE}}`

- Láncszabály törlése:

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Egy adott táblázat iptables-konfigurációjának mentése egy fájlba:

`sudo iptables-save -t {{tablename}} > {{path/to/iptables_file}}`

- Az iptables konfiguráció visszaállítása egy fájlból:

`sudo iptables-restore < {{path/to/iptables_file}}`
