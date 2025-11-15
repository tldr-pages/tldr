# sc_wartsfilter

> Select specific records from a `warts` file.
> More information: <https://www.caida.org/catalog/software/scamper/>.

- Filter all data records that had specific destinations and write them to a separate file:

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{192.0.2.5}} -a {{192.0.2.6}}`

- Filter all records that had certain destinations in a prefix and write them to a separate file:

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{2001:db8::/32}}`

- Filter all records that using a specific action and output them as JSON:

`sc_wartsfilter -i {{path/to/input.warts}} -t {{ping}} | sc_warts2json`
