# docker secret

> Gérer les secrets de Docker swarm.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/secret/>.

- Créer un nouveau secret depuis l'entrée standard :

`{{commande}} | docker secret create {{nom_du_secret}} -`

- Créer un nouveau secret depuis un fichier :

`docker secret create {{nom_du_secret}} {{chemin/vers/fichier}}`

- Lister tous les secrets :

`docker secret ls`

- Afficher des informations détaillées sur un ou plusieurs secrets dans un format humain :

`docker secret inspect --pretty {{nom_du_secret1 nom_du_secret2 ...}}`

- Supprimer un ou plusieurs secrets :

`docker secret rm {{nom_du_secret1 nom_du_secret2 ...}}`
