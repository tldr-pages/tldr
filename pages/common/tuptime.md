# tuptime

> Report historical and statistical real time of the system, preserving it between restarts.
> Like `uptime`, but extended with startups count, graceful and bad shutdowns, uptime/downtime percentages, and averages since first boot.
> More information: <https://github.com/rfmoz/tuptime>.

- Show system uptime history and statistics:

`tuptime`

- Show system lifetime as table:

`tuptime --table`

- Show system lifetime as list:

`tuptime --list`

- Show table with kernel version and boot ID:

`tuptime --table --kernel --bootid`

- Report from startup range:

`tuptime --table --since {{1}} --until {{5}}`

- Limit the report from a given number of seconds ago (e.g. one year = 31557600):

`tuptime --tsince -{{31557600}}`

- Output time in seconds and datetimes in epoch format:

`tuptime --seconds`

- Report in CSV format:

`tuptime --csv`
