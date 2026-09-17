# docker secret

> Gére les secrets de Docker swarm.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/secret/>.

- Crée un nouveau secret depuis l'entrée standard :

`{{commande}} | docker secret create {{nom_du_secret}} -`

- Crée un nouveau secret depuis un fichier :

`docker secret create {{nom_du_secret}} {{chemin/vers/fichier}}`

- Liste tous les secrets :

`docker secret ls`

- Affiche des informations détaillées sur un ou plusieurs secrets dans un format humain :

`docker secret inspect --pretty {{nom_du_secret1 nom_du_secret2 ...}}`

- Supprime un ou plusieurs secrets :

`docker secret rm {{nom_du_secret1 nom_du_secret2 ...}}`
