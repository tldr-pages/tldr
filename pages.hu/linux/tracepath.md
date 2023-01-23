# tracepath

> Nyomon követi az útvonalat egy hálózati állomáshoz, amely az MTU-t fedezi fel ezen az útvonalon. További információ: <https://manned.org/tracepath>.

- Egy előnyben részesített módja egy állomáshoz vezető útvonal nyomon követésének:

`tracepath -p {{33434}} {{host}}`

- Adja meg a kezdeti célportot, hasznos nem szabványos tűzfalbeállítások esetén:

`tracepath -p {{destination_port}} {{host}}`

- Nyomtassa ki mind az állomásneveket, mind a numerikus IP-címeket:

`tracepath -b {{host}}`

- Maximális TTL (ugrásszám) megadása:

`tracepath -m {{max_hops}} {{host}}`

- A kezdeti csomaghossz megadása (alapértelmezett érték 65535 IPv4 esetén és 128000 IPv6 esetén):

`tracepath -l {{packet_length}} {{host}}`

- Csak IPv6-címek használata:

`tracepath -6 {{host}}`
