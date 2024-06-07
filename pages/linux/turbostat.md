# turbostat

> Report processor topology, frequency, temperature, power, and idle statistics.
> More information: <https://manned.org/turbostat.8>.

- Display help:

`turbostat --help`

- Display statistics every 5 seconds:

`sudo turbostat`

- Display statistics every `interval` seconds:

`sudo turbostat -i {{interval}}`

- Do not decode and print the system configuration header information:

`sudo turbostat --quiet`

- Display useful information about cpu every 1 second, without header information:

`sudo turbostat --quiet --interval 1 --cpu 0-{{cpu_count}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`
