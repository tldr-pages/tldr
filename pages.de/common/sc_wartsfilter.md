# sc_wartsfilter

> Filtert bestimmte Datensätze aus einer `warts`-Datei.
> Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Filtere alle Datensätze, welche ein bestimmtes Ziel haben und schreibe sie in eine separate Datei:

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{192.0.2.5}} -a {{192.0.2.6}}`

- Filtere alle Datensätze, welche ein Ziel in einem bestimmten Prefix haben und schreibe sie in eine separate Datei:

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{2001:db8::/32}}`

- Filtere alle Datensätze, welche durch eine bestimmte Aktion entstanden sind und gebe sie als JSON aus:

`sc_wartsfilter -i {{path/to/input.warts}} -t {{ping}} | sc_warts2json`
