# docker image save

> Exporte une ou plusieurs images Docker dans une archive.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/save/>.

- Sauvegarde une image en redirigeant la sortie standard vers une archive `.tar` :

`docker {{[save|image save]}} {{image}}:{{étiquette}} > {{chemin/vers/fichier.tar}}`

- Sauvegarde une image dans une archive `.tar` :

`docker {{[save|image save]}} {{[-o|--output]}} {{chemin/vers/fichier.tar}} {{image}}:{{étiquette}}`

- Sauvegarde toutes les étiquettes de l'image :

`docker {{[save|image save]}} {{[-o|--output]}} {{chemin/vers/fichier.tar}} {{nom_image}}`

- Sélectionne des étiquettes particulières d'une image à sauvegarder :

`docker {{[save|image save]}} {{[-o|--output]}} {{chemin/vers/fichier.tar}} {{nom_image:etiquette1 nom_image:etiquette2 ...}}`
