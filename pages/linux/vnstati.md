# vnstati

> PNG image output support for vnStat.
> More information: <https://manned.org/vnstati>.

- Output a summary of the last 2: months, days, and all-time:

`vnstati --summary --iface {{network_interface}} --output {{path/to/output.png}}`

- Output the 10 most traffic-intensive days of all time:

`vnstati --top10 --iface {{network_interface}} --output {{path/to/output.png}}`

- Output monthly traffic statistics from the last 12 months:

`vnstati --months --iface {{network_interface}} --output {{path/to/output.png}}`

- Output hourly traffic statistics from the last 24 hours:

`vnstati --hours --iface {{network_interface}} --output {{path/to/output.png}}`
