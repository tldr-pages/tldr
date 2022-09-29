# docker-slim

> Analyser et optimiser les images Docker.
> Plus d'informatiosn : <https://github.com/docker-slim/docker-slim>.

- Démarrer DockerSlim en mode interactif :

`docker-slim`

- Analyser les couches Docker à partir d'une image spécifique :

`docker-slim xray --target {{image:etiquette}}`

- Linter un Dockerfile :

`docker-slim lint --target {{chemin/vers/Dockerfile}}`

- Analyser et générer une image Docker optimisée :

`docker-slim build {{image:etiquette}}`

- Afficher l'aide pour une sous-commande :

`docker-slim {{subcommande}} --help`
