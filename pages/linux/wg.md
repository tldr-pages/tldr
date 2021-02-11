# wg

> Manage the configuration of WireGuard interfaces.
> More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`sudo wg`

- Print out a new private key:

`wg genkey`

- Print out a new public key:

`echo {{private_key}} | wg pubkey`

- Generate a public and private key into files:

`wg genkey | tee {{privatekey}} | wg pubkey > {{publickey}}`
