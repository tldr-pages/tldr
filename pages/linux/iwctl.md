# iwctl

> A command-line tool for controlling the iwd network supplicant.
> More information: <https://iwd.wiki.kernel.org/gettingstarted>.

- Start the interactive mode, in this mode you can enter the commands directly, with autocompletion:

`iwctl`

- Call general help:

`iwctl --help`

- Display your Wi-Fi stations:

`iwctl station list`

- Start looking for networks with a station:

`iwctl station {{station}} scan`

- Display the networks found by a station:

`iwctl station {{station}} get-networks`

- Connect to a network with a station, if credentials are needed they will be asked:

`iwctl station {{station}} connect {{network_name}}`
