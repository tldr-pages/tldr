# useradd

> Crée un nouvel utilisateur:

- Crée un nouvel utilisateur:

`useradd {{name}}`

- Crée un nouvel utilisateur avec un dossier home par défaut:

`useradd --create-home {{name}}`

- Crée un nouvel utilisateur avec le shell spécifié:

`useradd --shell {{/path/to/shell}} {{name}}`

- Crée un nouvel utilisateur qui appartient aux groupes supplémentaires (attention à l'omission des espaces):

`useradd --groups {{group1,group2}} {{name}}`

- Crée un nouvel utilisateuri sans un dossier home:

`useradd --no-create-home --system {{name}}`
