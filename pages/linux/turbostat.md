# turbostat

> Report processor topology, frequency, temperature, power, and idle statistics.
> More information: <https://manned.org/turbostat.8>.

- Display statistics every 5 seconds:

`sudo turbostat`

- Display statistics every specified amount of seconds:

`sudo turbostat -i {{interval}}`

- Do not decode and print the system configuration header information:

`sudo turbostat --quiet`

- Display useful information about cpu every 1 second, without header information:

`sudo turbostat --quiet --interval 1 --cpu 0-{{cpu_thread_count}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- Display help:

`turbostat --help`
