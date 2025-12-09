# ssh-keyscan

> Récupère les clés SSH publiques de machines distantes.
> Plus d'informations : <https://man.openbsd.org/ssh-keyscan>.

- Récupère toutes les clés d'une machine distante :

`ssh-keyscan {{hote_distant}}`

- Récupère toutes les clés d'une machine distante en écoutant sur un port particulier :

`ssh-keyscan -p {{port}} {{hote_distant}}`

- Récupère un type particulier de clés d'une machine distante :

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{hote_distant}}`

- Met à jour manuellement le fichier `known_hosts` des hôtes connus avec l'empreinte d'une :

`ssh-keyscan -H {{hote_distant}} >> ~/.ssh/known_hosts`
