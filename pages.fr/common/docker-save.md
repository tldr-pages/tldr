# docker save

> Exporeter une ou plusieurs images Docker dans une archive.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/save/>.

- Sauvegarder une image en redirigeant la sortie standard vers une archive tar :

`docker save {{image}}:{{etquette}} > {{chemin/vers/fichier.tar}}`

- Sauvegarder une image dans une archive tar :

`docker save --output {{chemin/vers/fichier.tar}} {{image}}:{{etquette}}`

- Sauvegarder toutes les étiquettes de l'image :

`docker save --output {{chemin/vers/fichier.tar}} {{nom_de_l_image}}`

- Sélectionner des étiquettes particulières d'une image à sauvegarder :

`docker save --output {{chemin/vers/fichier.tar}} {{nom_de_l_image:etquette1 nom_de_l_image:etquette2 ...}}`
