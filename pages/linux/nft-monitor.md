# nft monitor

> Monitor netfilter events in real time using nftables.
> Displays live changes to rules, tables, sets, counters, and packet flow.
> Requires `nftables` and kernel NFTRACE/NFTABLES support.

- Monitor all nftables events:

`sudo nft monitor`

- Monitor only rule updates (add, delete, replace):

`sudo nft monitor rule`

- Monitor table and chain creation/deletion:

`sudo nft monitor netdev`

- Monitor set and element updates:

`sudo nft monitor set`

- Monitor flowtable operations:

`sudo nft monitor flowtable`

- Monitor events and print JSON output:

`sudo nft --json monitor`
