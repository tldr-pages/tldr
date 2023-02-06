# dumpcap

> Hálózati adatforgalom-dömping eszköz. További információ: <https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- A rendelkezésre álló interfészek megjelenítése:

`dumpcap --list-interfaces`

- Csomagok rögzítése egy adott interfészen:

`dumpcap --interface {{1}}`

- Csomagok rögzítése egy adott helyre:

`dumpcap --interface {{1}} -w {{path/to/output_file.pcapng}}`

- Írás egy meghatározott méretű gyűrűpufferbe egy adott maximális fájllimit mellett:

`dumpcap --interface {{1}} -w {{path/to/output_file.pcapng}} --ring-buffer filesize:{{500000}} --ring-buffer files:{{10}}`
