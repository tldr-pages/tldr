# conda

> Gestion des paquets, des dépendances et des environnements pour tout langage de programmation.

> Certaines sous-commandes comme `create` ont leur propre documentation.

> Voir aussi : `mamba`.

> Plus d'informations : <https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- Crée un nouvel environnement en y installant les paquets nommés :

`conda create {{[-n|--name]}} {{nom_environnement}} {{python=3.9 matplotlib}}`

- Liste tous les environnements :

`conda info {{[-e|--envs]}}`

- Active un environnement :

`conda activate {{nom_environnement}}`

- Désactive un environnement :

`conda deactivate`

- Supprime un environnement (supprime tous les paquets) :

`conda remove {{[-n|--name]}} {{nom_environnement}} --all`

- Installe des paquets dans l'environnement courant :

`conda install {{python=3.4 numpy}}`

- Liste les paquets actuellement installés dans l'environnement courant :

`conda list`

- Supprime les paquets et caches inutilisés :

`conda clean {{[-a|--all]}}`

