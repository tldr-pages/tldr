# nft monitor

> Show real-time changes happening inside the Linux firewall (nftables).
> Useful for seeing when rules, tables, or packets change.
> More information: <https://manned.org/nft#head21>.

- Monitor all nftables events:

`sudo nft monitor`

- Monitor only rule updates (add, delete, replace):

`sudo nft monitor rules`

- Monitor set and element updates:

`sudo nft monitor sets`

- Monitor events and print JSON output:

`sudo nft {{[-j|--json]}} monitor`
