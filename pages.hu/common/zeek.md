# zeek

> Passzív hálózati forgalomelemző. A kimeneti és naplófájlok az aktuális munkakönyvtárba kerülnek mentésre. További információ: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- Élő forgalom elemzése egy hálózati interfészről:

`sudo zeek --iface {{interface}}`

- Élő forgalom elemzése egy hálózati interfészről és egyéni szkriptek betöltése:

`sudo zeek --iface {{interface}} {{script1}} {{script2}}`

- Élő forgalom elemzése egy hálózati interfészről, szkriptek betöltése nélkül:

`sudo zeek --bare-mode --iface {{interface}}`

- Élő forgalom elemzése egy hálózati interfészről, a `tcpdump` szűrő alkalmazásával:

`sudo zeek --filter {{path/to/filter}} --iface {{interface}}`

- Élő forgalom elemzése egy hálózati interfészről watchdog időzítő használatával:

`sudo zeek --watchdog --iface {{interface}}`

- A `pcap` fájlból származó forgalom elemzése:

`zeek --readfile {{path/to/file.trace}}`
