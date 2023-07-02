# docker start

> Lancer un ou plusieurs conteneurs arrêtés.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/start/>.

- Afficher l'aide :

`docker start`

- Lancer un conteneur docker :

`docker start {{conteneur}}`

- Lancer un conteneur, en attachant `stdout` et `stderr` et en transférant les signaux :

`docker start --attach {{conteneur}}`

- Lancer un ou plusieurs conteneurs séparés par des espaces :

`docker start {{conteneur1 conteneur2 ...}}`
