# install

> Copie des fichiers et mets à jour leurs attributs.
> Copie des fichiers (souvent des exécutables) dans un repertoire système comm `/usr/local/bin` et leur donne les permissions et propriétaires appropriés.

- Copie des fichiers vers un destination:

`install {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur propriétaire:

`install -o {{user}} {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur groupe d'appartenance:

`install -g {{user}} {{path/to/source}} {{path/to/destination}}`

- Copie des fichiers vers une destination en mettant à jour leur mode:

`install -m {{+x}} {{path/to/source}} {{path/to/destination}}`

- Copie des fichier et met à jour leurs date d'accès et de modification à partir de leur source respective:

`install -p {{path/to/source}} {{path/to/destination}}`
