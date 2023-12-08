# docker load

> Charge des images docker depuis des fichiers ou `stdin`.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/load/>.

- Charge une image docker depuis `stdin` :

`docker load < {{chemin/vers/fichier_image.tar}}`

- Charge une image docker depuis un fichier spécifique :

`docker load --input {{chemin/vers/fichier_image.tar}}`

- Charge une image docker depuis un fichier spécifique en mode silencieux :

`docker load --quiet --input {{chemin/vers/fichier_image.tar}}`
