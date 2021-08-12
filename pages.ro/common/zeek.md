# zeek

> Analizor pasiv de trafic în rețea.
> Toate fișierele de ieșire și jurnal vor fi salvate în directorul de lucru curent.
> Mai multe informaţii: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>

- Analizați traficul live dintr-o interfață de rețea:

`sudo zeek --iface {{interface}}`

- Analizați traficul live dintr-o interfață de rețea și încărcați scripturi personalizate:

`sudo zeek --iface {{interface}} {{script1}} {{script2}}`

- Analizați traficul live dintr-o interfață de rețea, fără a încărca scripturi:

`sudo zeek --bare-mode --iface {{interface}}`

- Analizați traficul live dintr-o interfață de rețea, aplicând un filtru `tcpdump:

`sudo zeek --filter {{path/to/filter}} --iface {{interface}}`

- Analizați traficul live dintr-o interfață de rețea folosind un cronometru watchdog:

`sudo zeek --watchdog --iface {{interface}}`

- Analizaţi traficul dintr-un fişier `pcap`:

`zeek --readfile {{path/to/file.trace}}`
