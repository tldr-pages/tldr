# pcapfix

> Repariere beschädigte oder korrumpierte `pcap`- und `pcapng`-Dateien.
> Weitere Informationen: <https://f00l.de/pcapfix/>.

- Repariere eine `pcap`/`pcapng`-Datei (Hinweis: bei `pcap`-Dateien werden nur die ersten 262144 Bytes jedes Pakets gescannt):

`pcapfix {{pfad/zu/datei.pcapng}}`

- Repariere eine ganze `pcap`-Datei:

`pcapfix --deep-scan {{pfad/zu/datei.pcap}}`

- Repariere eine `pcap`/`pcapng`-Datei und schreibe die Reparieree Datei an einen bestimmten Speicherort:

`pcapfix --outfile {{pfad/zu/Repariere.pcap}} {{pfad/zu/datei.pcap}}`

- Behandle die zu reparierende Datei als `pcapng`-Datei, unabhängig von der automatischen Typenerkennung:

`pcapfix --pcapng {{pfad/zu/datei.pcapng}}`

- Repariere eine Datei und zeige den Reparaturprozess im Detail:

`pcapfix --verbose {{pfad/zu/datei.pcap}}`
