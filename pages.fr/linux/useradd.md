# useradd

> Crée un nouvel utilisateur.
> Voir aussi `users`, `userdel`, `usermod`.
> Plus d'informations : <https://manned.org/useradd>.

- Crée un nouvel utilisateur :

`sudo useradd {{nom_utilisateur}}`

- Crée un nouvel utilisateur en spéficiant un identifiant numérique particulier :

`sudo useradd --uid {{identifiant}} {{nom_utilisateur}}`

- Crée un nouvel utilisateur avec le shell spécifié :

`sudo useradd --shell {{chemin/vers/shell}} {{nom_utilisateur}}`

- Crée un nouvel utilisateur qui appartient aux groupes supplémentaires (attention à l'omission des espaces) :

`sudo useradd --groups {{groupe1,groupe2,...}} {{nom_utilisateur}}`

- Crée un nouvel utilisateur avec le répertoire personnel par défaut :

`sudo useradd --create-home {{nom_utilisateur}}`

- Crée un nouvel utilisateur avec un répertoire personnel rempli par les fichiers et répertoires d'un répertoire squelette :

`sudo useradd --skel {{chemin/vers/repertoire_squelette}} --create-home {{nom_utilisateur}}`

- Crée un nouvel utilisateur système sans répertoire personnel :

`sudo useradd --system {{nom_utilisateur}}`
