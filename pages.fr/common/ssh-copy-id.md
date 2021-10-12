# ssh-copy-id

> Dépose une clé publique sur une machine distante, dans les clés autorisées `authorized_keys`.
> Plus d'informations : <https://manned.org/ssh-copy-id>.

- Déposer toutes les clés publiques sur la machine distante :

`ssh-copy-id {{nom_utilisateur@hote_distant}}`

- Déposer une clé publique spécifique sur la machine distante :

`ssh-copy-id -i {{chemin/vers/certificat}} {{nom_utilisateur}}@{{hote_distant}}`

- Déposer une clé publique spécifique sur la machine distante en utilisant un port particulier :

`ssh-copy-id -i {{chemin/vers/certificat}} -p {{port}} {{nom_utilisateur}}@{{hote_distant}}`
