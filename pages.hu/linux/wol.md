# wol

> Wake-on-LAN varázscsomagok küldésére szolgáló ügyfél. További információ: <https://sourceforge.net/projects/wake-on-lan/>.

- WoL csomag küldése egy eszköznek:

`wol {{mac_address}}`

- WoL csomag küldése egy másik alhálózatban lévő eszköznek annak IP címe alapján:

`wol --ipaddr={{ip_address}} {{mac_address}}`

- WoL-csomag küldése egy másik alhálózatban lévő eszköznek annak hostneve alapján:

`wol --host={{hostname}} {{mac_address}}`

- WoL-csomag küldése egy adott portra egy állomáson:

`wol --port={{port_number}} {{mac_address}}`

- Hardvercímek, IP-címek/hostnevek, opcionális portok és SecureON-jelszavak beolvasása egy fájlból:

`wol --file={{path/to/file}}`

- Szöveges kimenet bekapcsolása:

`wol --verbose {{mac_address}}`
