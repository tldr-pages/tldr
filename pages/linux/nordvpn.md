# nordvpn

> Command-line interface for NordVPN.
> More information: <https://support.nordvpn.com/hc/en-us/articles/20196094470929-Installing-NordVPN-on-Linux-distributions>.

- Interactively log into a NordVPN account:

`nordvpn login`

- Display the connection status:

`nordvpn status`

- Connect to the nearest NordVPN server:

`nordvpn {{[c|connect]}}`

- List all available countries:

`nordvpn countries`

- Connect to a NordVPN server in a specific country:

`nordvpn {{[c|connect]}} {{Germany}}`

- Connect to a NordVPN server in a specific country and city:

`nordvpn {{[c|connect]}} {{Germany}} {{Berlin}}`

- Set autoconnect option:

`nordvpn {{[s|set]}} autoconnect on`
