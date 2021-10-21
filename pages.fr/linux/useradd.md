# useradd

> Crée un nouvel utilisateur.
> Plus d'informations : <https://manned.org/useradd>.

- Crée un nouvel utilisateur :

`useradd {{nom}}`

- Crée un nouvel utilisateur avec un dossier home par défaut :

`useradd --create-home {{nom}}`

- Crée un nouvel utilisateur avec le shell spécifié :

`useradd --shell {{/chemin/vers/shell}} {{nom}}`

- Crée un nouvel utilisateur qui appartient aux groupes supplémentaires (attention à l'omission des espaces) :

`useradd --groups {{groupe1,groupe2}} {{nom}}`

- Crée un nouvel utilisateur sans un dossier home :

`useradd --no-create-home --system {{nom}}`
