# conntrack

> Interact with the Netfilter connection tracking system.
> Search, list, inspect, modify, and delete connection flows.
> More information: <https://manned.org/conntrack>.

- List all currently tracked connections:

`conntrack {{[-L|--dump]}}`

- Display a real-time event log of connection changes:

`conntrack {{[-E|--event]}}`

- Display a real-time event log of connection changes and associated timestamps:

`conntrack {{[-E|--event]}} {{[-o|--output]}} timestamp`

- Display a real-time event log of connection changes for a specific IP address:

`conntrack {{[-E|--event]}} {{[-s|--orig-src]}} {{ip_address}}`

- Delete all flows for a specific source IP address:

`conntrack {{[-D|--delete]}} {{[-s|--orig-src]}} {{ip_address}}`
