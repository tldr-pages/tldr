# wg

> Gestion de la configuration des interfaces WireGuard.
> Plus d'informations : <https://www.wireguard.com/quickstart/>.

- Vérifier l'état des interfaces actuellement actives :

`wg`

- Générer une clé privée :

`wg genkey`

- Générer une clé publique à partir d'une clé privée :

`wg pubkey < {{chemin/vers/clé_privée}} > {{chemin/vers/clé_publique}}`

- Générer une clé publique et privée :

`wg genkey | tee {{chemin/vers/clé_privée}} | wg pubkey > {{chemin/vers/clé_publique}}`

- Afficher la configuration actuelle d'une interface wireguard :

`wg showconf {{wg0}}`
