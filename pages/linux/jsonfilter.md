# jsonfilter

> Extract values from JSON on OpenWrt with JsonPath patterns.
> Patterns support `$`, `@`, `[]`, `*`, and the union operator `,`. They do not support `..` or script filters.
> More information: <https://github.com/openwrt/jsonpath>.

- Print the release description from `ubus`:

`ubus call system board | jsonfilter -e '@.release.description'`

- Print the first IPv4 address on the `lan` interface:

`ifstatus lan | jsonfilter -e '@["ipv4-address"][0].address'`

- Print the name of every network interface that is up:

`ubus call network.interface dump | jsonfilter -e '@.interface[@.up=true].interface'`

- Export two counters for `eval` in the shell:

`devstatus br-lan | jsonfilter -e 'RX=@.statistics.rx_bytes' -e 'TX=@.statistics.tx_bytes'`

- Read JSON from a file and print the values matched by a pattern:

`jsonfilter -i {{path/to/file.json}} -e '{{pattern}}'`

- Read a JSON string instead of `stdin`:

`jsonfilter -s "{{json}}" -e '{{pattern}}'`

- Display help:

`jsonfilter -h`
