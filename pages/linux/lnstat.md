# lnstat

> Display Linux network statistics from `/proc/net/stat`.
> See also: `nstat`, `ss`.
> More information: <https://manned.org/lnstat>.

- Display all network statistics, refreshing every 3 seconds:

`lnstat`

- List the available statistics files and their keys:

`lnstat {{[-d|--dump]}}`

- Display statistics from a specific file:

`lnstat {{[-f|--file]}} {{arp_cache|ndisc_cache|rt_cache|...}}`

- Display specific keys from a file:

`lnstat {{[-k|--keys]}} {{arp_cache:entries,arp_cache:allocs}}`

- Display statistics at a specific interval a specific number of times:

`lnstat {{[-i|--interval]}} {{seconds}} {{[-c|--count]}} {{count}}`

- Display statistics in JSON format:

`lnstat {{[-j|--json]}}`
