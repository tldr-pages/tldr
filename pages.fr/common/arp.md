# arp

> Affiche et manipule votre cache système ARP.
> Plus d'informations : <https://manned.org/arp>.

- Affiche la table ARP courante :

`arp -a`

- Nettoie le cache :

`sudo arp -a -d`

- Supprime une entrée spécifique :

`arp -d {{adresse}}`

- Crée une entré dans la table ARP:

`arp -s {{adresse}} {{adresse_mac}}`
