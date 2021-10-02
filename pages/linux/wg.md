# wg

> Manage the configuration of WireGuard interfaces.
> More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`wg`

- Generate a new private key:

`wg genkey`

- Generate a public key from a private key:

`wg pubkey < {{private_key}} > {{public_key}}`

- Generate a public and private key:

`wg genkey | tee {{private_key}} | wg pubkey > {{public_key}}`
