# adduser

> Outil d'ajout d'utilisateurs.
> Plus d'informations : <https://manpages.debian.org/latest/adduser/adduser.html>.

- Crée un nouvel utilisateur avec un répertoire personnel générique et demande interactivement un mot de passe :

`adduser {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur sans répertoire personnel :

`adduser --no-create-home {{nom_dutilisateur}}`

- Crée un nouvel utilisateur avec un répertoire personnel correspondant au dossier spécifié :

`adduser --home {{chemin/vers/dossier}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur avec l'interpréteur de commandes spécifié comme interpréteur de commandes de connexion :

`adduser --shell {{chemin/vers/shell}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur appartenant au groupe donné :

`adduser --ingroup {{groupe}} {{nom_d_utilisateur}}`
