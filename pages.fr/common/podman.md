# podman

> Outil de gestion simple pour les pods, conteneurs et images.
> Podman fournit une interface en ligne de commande comparable à Docker. En résumé : `alias docker=podman`.
> Plus d'informations : <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Liste tous les conteneurs (en cours d'exécution et arrêtés) :

`podman ps {{[-a|--all]}}`

- Crée un conteneur à partir d'une image, avec un nom personnalisé :

`podman run --name {{nom_conteneur}} {{image}}`

- Démarre ou arrête un conteneur existant :

`podman {{start|stop}} {{nom_conteneur}}`

- Télécharge une image depuis un registre (par défaut Docker Hub) :

`podman pull {{image}}`

- Affiche la liste des images déjà téléchargées :

`podman images`

- Ouvre un shell dans un conteneur déjà en cours d'exécution :

`podman exec {{[-it|--interactive --tty]}} {{nom_conteneur}} {{sh}}`

- Supprime un conteneur arrêté :

`podman rm {{nom_conteneur}}`

- Affiche les journaux d'un ou plusieurs conteneurs et suit la sortie en continu :

`podman logs {{[-f|--follow]}} {{nom_conteneur}} {{identifiant_conteneur}}`
