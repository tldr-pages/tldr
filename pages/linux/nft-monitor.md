# nft monitor

> Monitor netfilter events in real time using nftables.
> Requires `nftables` and kernel NFTRACE/NFTABLES support.
> More information: <https://manned.org/nft#head21>.

- Monitor all nftables events:

`sudo nft monitor`

- Monitor only rule updates (add, delete, replace):

`sudo nft monitor rules`

- Monitor table and chain creation/deletion:

`sudo nft monitor netdev`

- Monitor set and element updates:

`sudo nft monitor sets`

- Monitor flowtable operations:

`sudo nft monitor flowtable`

- Monitor events and print JSON output:

`sudo nft {{[-j|--json]}} monitor`
