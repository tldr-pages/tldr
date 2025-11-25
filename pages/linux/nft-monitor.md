# nft monitor

> Monitor netfilter events in real time using nftables.
> Requires `nftables` and kernel NFTRACE/NFTABLES support.
> More information: <https://manned.org/nft#head21>.

- Monitor all nftables events:

`sudo nft monitor`

- Monitor only rule updates (add, delete, replace):

`sudo nft monitor rules`

- Monitor set and element updates:

`sudo nft monitor sets`

- Monitor events and print JSON output:

`sudo nft {{[-j|--json]}} monitor`
