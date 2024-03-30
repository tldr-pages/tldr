# docker load

> Charge des images Docker depuis des fichiers ou `stdin`.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/load/>.

- Charge une image Docker depuis `stdin` :

`docker load < {{chemin/vers/fichier_image.tar}}`

- Charge une image Docker depuis un fichier spécifique :

`docker load --input {{chemin/vers/fichier_image.tar}}`

- Charge une image Docker depuis un fichier spécifique en mode silencieux :

`docker load --quiet --input {{chemin/vers/fichier_image.tar}}`
