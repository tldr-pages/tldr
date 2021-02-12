# wg

> Manage the configuration of WireGuard interfaces.
> More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`sudo wg`

- Print a new private key:

`wg genkey`

- Print a new public key:

`echo {{private_key}} | wg pubkey`

- Generate a public and private key:

`wg genkey | tee {{privatekey.txt}} | wg pubkey > {{publickey.txt}}`
