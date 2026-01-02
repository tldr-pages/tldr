# docker image load

> Charge des images Docker depuis des fichiers ou `stdin`.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/load/>.

- Charge une image Docker depuis `stdin` :

`docker < {{chemin/vers/fichier_image.tar}} {{[load|image load]}}`

- Charge une image Docker depuis un fichier spécifique :

`docker {{[load|image load]}} {{[-i|--input]}} {{chemin/vers/fichier_image.tar}}`

- Charge une image Docker depuis un fichier spécifique en mode silencieux :

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{chemin/vers/fichier_image.tar}}`
