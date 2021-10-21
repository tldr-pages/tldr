# usermod

> Modifie un compte utilisateur.
> Plus d'informations : <https://manned.org/usermod>.

- Change le nom d'un utilisateur :

`usermod -l {{nouveau_nom}} {{utilisateur}}`

- Ajoute l'utilisateur à des groupes supplémentaires (attention à l'omission d'espaces) :

`usermod -a -G {{groupe1,groupe2}} {{utilisateur}}`

- Crée un nouveau dossier home pour un utilisateur et déplace ses fichiers vers celui-ci :

`usermod -m -d {{/chemin/vers/home}} {{utilisateur}}`
