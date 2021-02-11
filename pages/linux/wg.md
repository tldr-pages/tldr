# wg

> Manage the configuration of WireGuard interfaces.
> More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`sudo wg`

- Print out a new private key:

`wg genkey`

- Print out a new public key:

`echo {{private_key}} | wg pubkey`

- Print out a new private and public key pair:

`wg genkey | tee /dev/tty | wg pubkey`
