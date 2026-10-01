# wg

> Gestion de la configuration des interfaces WireGuard.
> Plus d'informations : <https://www.wireguard.com/quickstart/>.

- Vérifie l'état des interfaces actuellement actives :

`sudo wg`

- Génère une clé privée :

`wg genkey`

- Génère une clé publique à partir d'une clé privée :

`wg < {{chemin/vers/clé_privée}} pubkey > {{chemin/vers/clé_publique}}`

- Génère une clé publique et privée :

`wg genkey | tee {{chemin/vers/clé_privée}} | wg pubkey > {{chemin/vers/clé_publique}}`

- Affiche la configuration actuelle d'une interface wireguard :

`sudo wg showconf {{wg0}}`
