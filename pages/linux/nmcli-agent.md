# nmcli agent

> Run nmcli as a NetworkManager secret agent or polkit agent.
> More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Register nmcli as a secret agent and listen for secret requests:

`nmcli agent secret`

- Register nmcli as a polkit agent and listen for authorization requests:

`nmcli agent polkit`

- Register nmcli as both a secret and a polkit agent:

`nmcli agent all`
