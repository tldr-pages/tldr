# iwctl

> Control the `iwd` network supplicant.
> See also: `nmcli`, `iw`.
> More information: <https://manned.org/iwctl>.

- Run `iwctl` in interactive mode:

`iwctl`

- Display Wi-Fi stations:

`iwctl station list`

- Look for networks with a station:

`iwctl station {{station}} scan`

- Display the networks found by a station:

`iwctl station {{station}} get-networks`

- Connect to a network with a station, if credentials are needed they will be asked:

`iwctl station {{station}} connect {{network_name}}`

- Display help:

`iwctl {{[-h|--help]}}`
