# install

> Copie des fichiers et mets à jour leurs attributs.
> Copie des fichiers (souvent des exécutables) dans un répertoire système comme `/usr/local/bin` et leur donne les permissions et propriétaires appropriés.

- Copie des fichiers vers une destination:

`install {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur propriétaire:

`install -o {{utilisateur}} {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur groupe d'appartenance:

`install -g {{utilisateur}} {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur mode:

`install -m {{+x}} {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers et met à jour leur date d'accès et de modification à partir de leur source respective:

`install -p {{path/to/source}} {{path/to/destination}}`
