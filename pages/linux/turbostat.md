# turbostat

> Report processor frequency and idle statistics.
> More information: <https://www.linux.org/docs/man8/turbostat.html>.

- Display usage for the most common parameters:

`turbostat --help`

- Display statistics every 5 seconds:

`sudo turbostat`

- Display statistics every i seconds:

`sudo turbostat -i {{i}}`

- Do not decode and print the system configuration header information:

`sudo turbostat --quiet`

- Display useful information about cpu every 1 second, without header information:

`sudo turbostat --quiet --interval 1 --cpu 0-{{cpu_count}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal" `

