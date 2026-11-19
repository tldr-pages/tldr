# useradd

> Crée un nouvel utilisateur.
> Voir aussi : `users`, `userdel`, `usermod`.
> Plus d'informations : <https://manned.org/useradd>.

- Crée un nouvel utilisateur :

`sudo useradd {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur en spéficiant un identifiant numérique particulier :

`sudo useradd {{[-u|--uid]}} {{identifiant}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur avec le shell spécifié :

`sudo useradd {{[-s|--shell]}} {{chemin/vers/shell}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur qui appartient aux groupes supplémentaires (attention à l'omission des espaces) :

`sudo useradd {{[-G|--groups]}} {{groupe1,groupe2,...}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur avec le répertoire personnel par défaut :

`sudo useradd {{[-m|--create-home]}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur avec un répertoire personnel rempli par les fichiers et répertoires d'un répertoire squelette :

`sudo useradd {{[-k|--skel]}} {{chemin/vers/repertoire_squelette}} {{[-m|--create-home]}} {{nom_d_utilisateur}}`

- Crée un nouvel utilisateur système sans répertoire personnel :

`sudo useradd {{[-r|--system]}} {{nom_d_utilisateur}}`
