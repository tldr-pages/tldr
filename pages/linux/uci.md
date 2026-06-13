# uci

> Manage OpenWrt configuration files.
> More information: <https://openwrt.org/docs/techref/uci>.

- Fetch a value:

`uci get {{network.lan.ipaddr}}`

- List all options and their values:

`uci show {{network}}`

- Set a value:

`uci set {{config}}.{{section}}.{{option}}={{value}}`

- Add a new section:

`uci add {{config}} {{section}}`

- Delete a section or value:

`uci delete {{config}}.{{section}}.{{option}}`

- Commit changes:

`uci commit {{config}}`

- Discard uncommitted changes:

`uci revert {{config}}`

- Display help:

`uci`
