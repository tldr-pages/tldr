# docker stats

> Affiché un flux en direct des statistiques d'utilisation des ressources pour les conteneurs.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/stats/>.

- Afficher un flux en direct des statistiques d'utilisation des ressources pour tous les conteneurs :

`docker stats`

- Afficher un flux en direct des statistiques d'utilisation des ressources pour un ou plusieurs conteneurs séparés par des espaces :

`docker stats {{nom_du_conteneur}}`

- Change le format de sortie pour afficher l'utilisation CPU du conteneur en pourcentage :

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Afficher les statistiques d'utilisation des ressources pour tous les conteneurs (y compris ceux qui ne sont pas en cours d'exécution) :

`docker stats --all`

- Desactiver le flux en direct des statistiques d'utilisation des ressources et afficher les statistiques une seule fois :

`docker stats --no-stream`
