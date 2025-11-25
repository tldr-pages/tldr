# nft trace

> Trace packet flow through nftables chains and rules in real time.
> Useful for debugging firewall behavior and understanding packet decisions.
> Requires nftables and kernel tracing support.
> More information: <https://manpages.debian.org/testing/nftables/nft.8.en.html>.

- Enable tracing for all packets passing through a specific hook:

`sudo nft trace add rule {{inet}} {{filter}} {{input}} {{counter}}`

- Enable tracing only for packets matching a specific expression (e.g., destination port):

`sudo nft trace add rule {{inet}} {{filter}} {{input}} tcp dport {{22}} {{counter}}`

- Trace packets flowing through a specific table and chain:

`sudo nft trace add chain {{inet}} {{filter}} {{input}}`

- Show live trace output from the kernel log:

`sudo dmesg -w | grep nft`

- Remove all trace rules:

`sudo nft trace delete ruleset`

- Inspect trace-related rules in the ruleset:

`nft list ruleset | grep trace`
