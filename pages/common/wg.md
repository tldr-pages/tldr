# wg

> Manage the configuration of WireGuard interfaces.
> More information: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`sudo wg`

- Check status of the specified interface:

`sudo wg show {{interface}}`

- Generate a new private key and print it to `stdout`:

`wg genkey`

- Generate a public key from a private key and print it to `stdout`:

`wg < {{path/to/private_key}} pubkey`

- Generate a public and private key and save them to files:

`wg genkey | tee {{path/to/private_key}} | wg pubkey > {{path/to/public_key}}`

- Generate a pre-shared key and print it to `stdout`:

`wg genpsk`

- Show the active configuration of an interface:

`sudo wg showconf {{interface}}`
