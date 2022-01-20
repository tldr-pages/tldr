# wg

> Manage the configuration of WireGuard interfaces.
> More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`wg`

- Generate a new private key:

`wg genkey`

- Generate a public key from a private key:

`wg pubkey < {{path/to/private_key}} > {{path/to/public_key}}`

- Generate a public and private key:

`wg genkey | tee {{path/to/private_key}} | wg pubkey > {{path/to/public_key}}`

- Show the current configuration of a wireguard interface:

`wg showconf {{wg0}}`
