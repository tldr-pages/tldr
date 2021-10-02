# wg

> Gestion de la configuration des interfaces WireGuard.
> Plus d'informations: <https://www.wireguard.com/quickstart/>.

- Check status of currently active interfaces:

`wg`

- Générer une clé privée :

`wg genkey`

- Générer une clé publique à partir d'une clé privée :

`wg pubkey < {{private_key}} > {{public_key}}`

- Générer une clé publique et privée :

`wg genkey | tee {{private_key}} | wg pubkey > {{public_key}}`
