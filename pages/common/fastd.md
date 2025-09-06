# fastd

> VPN daemon.
> Works on Layer 2 or Layer 3, supports different encryption methods, used by Freifunk.
> See also: `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`.
> More information: <https://fastd.readthedocs.io/en/stable/>.

- Start `fastd` with a specific configuration file:

`fastd {{[-c|--config]}} {{path/to/fastd.conf}}`

- Start a Layer 3 VPN with an MTU of 1400, loading the rest of the configuration parameters from a file:

`fastd {{[-m|--mode]}} {{tap}} {{[-M|--mtu]}} {{1400}} {{[-c|--config]}} {{path/to/fastd.conf}}`

- Validate a configuration file:

`fastd --verify-config {{[-c|--config]}} {{path/to/fastd.conf}}`

- Generate a new keypair:

`fastd --generate-key`

- Show the public key to a private key in a configuration file:

`fastd --show-key {{[-c|--config]}} {{path/to/fastd.conf}}`

- Show the current version:

`fastd {{[-v|--version]}}`
