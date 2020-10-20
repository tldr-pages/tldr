# usermod

> Modifie un compte utilisateur.

- Change le nom d'un utilisateur:

`usermod -l {{newname}} {{user}}`

- Ajoute l'utilisateur à des groupes supplementaires (attention à l'omission d'espaces):

`usermod -a -G {{group1,group2}} {{user}}`

- Crée un nouveau dossier home pour un utilisateur et déplace ses fichiers vers celui-ci:

`usermod -m -d {{/path/to/home}} {{user}}`
