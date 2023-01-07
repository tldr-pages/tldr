# conntrack

> Interact with the Netfilter connection tracking system.
> Search, list, inspect, modify, and delete connection flows.
> More information: <https://manned.org/conntrack>.

- List all currently tracked connections:

`conntrack --dump`

- Display a real-time event log of connection changes:

`conntrack --event`

- Display a real-time event log of connection changes and associated timestamps:

`conntrack --event -o timestamp`

- Display a real-time event log of connection changes for a specific IP address:

`conntrack --event --orig-src {{ip_address}}`

- Delete all flows for a specific source IP address:

`conntrack --delete --orig-src {{ip_address}}`
