# ss

> Segédprogram aljzatok vizsgálatára. További információ: <https://manned.org/ss.8>.

- Az összes TCP/UDP/RAW/UNIX aljzat megjelenítése:

`ss -a {{-t|-u|-w|-x}}`

- TCP aljzatok szűrése állapotok szerint, csak/kivéve:

`ss {{state/exclude}} {{bucket/big/connected/synchronized/...}}`

- A helyi HTTPS porthoz (443) csatlakozó összes TCP aljzat megjelenítése:

`ss -t src :{{443}}`

- A helyi 8080-as porton figyelő összes TCP-aljzat megjelenítése:

`ss -lt src :{{8080}}`

- Az összes TCP aljzat megjelenítése a távoli ssh porthoz csatlakozó folyamatokkal együtt:

`ss -pt dst :{{ssh}}`

- Az összes UDP aljzat megjelenítése, amely egy adott forrás- és célporton csatlakozik:

`ss -u 'sport == :{{source_port}} and dport == :{{destination_port}}'`

- A 192.168.0.0/16 alhálózaton helyileg csatlakozó összes TCP IPv4 aljzat megjelenítése:

`ss -4t src {{192.168/16}}`

- IPv4 vagy IPv6 Socket kapcsolat kiiktatása 192.168.1.17 cél-IP címmel és 8080-as célporttal:

`ss --kill dst {{192.168.1.17}} dport = {{8080}}`
