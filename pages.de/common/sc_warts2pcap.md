# sc_warts2pcap

> Schreibt die in den `warts`-Dateien enthaltenen Pakete in eine `pcap`-Datei.
> Dies ist nur bei tbit, sting und sniff möglich.
> Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Wandle die Daten aus mehreren `warts`-Dateien in eine `pcap`-Datei um:

`sc_warts2pcap -o {{path/to/output.pcap}} {{path/to/file1.warts path/to/file2.warts ...}}`

- Wandle die Daten aus einer `warts`-Datei in eine `pcap`-Datei um und sortiere die Pakete nach Zeitstempel:

`sc_warts2pcap -s -o {{path/to/output.pcap}} {{path/to/file.warts}}`
