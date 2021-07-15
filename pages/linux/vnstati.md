# vnstati

> PNG image output support for vnStat.
> More information: <https://manned.org/vnstati>.

- Output a summary of the last 2: months, days, and all-time:

`vnstati --summary --iface {{network_interface}} --output {{output.png}}`

- Output all-time top 10 traffic days:

`vnstati --top10 --iface {{network_interface}} --output {{output.png}}`

- Output monthly traffic statistics from the last 12 months:

`vnstati --months --iface {{network_interface}} --output {{output.png}}`

- Output traffic statistics on an hourly basis for the last 24 hours:

`vnstati --hours --iface {{network_interface}} --output {{output.png}}`
