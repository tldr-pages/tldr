# assimp

> Client en ligne de commande pour l'Open Asset Import Library.
> Supporte le chargement de plus de 40 formats de fichiers 3D, et exporte vers quelques formats 3D populaire.
> Plus d'informations : <http://www.assimp.org/>.

- Liste tous les formats d'import supportés :

`assimp listext`

- Liste tous les formats de sortie supportés :

`assimp listexport`

- Convertis un fichier vers un format de sortie supporté, avec les paramètres par défaut :

`assimp export {{fichier_d_entrée.stl}} {{fichier_de_sortie.obj}}`

- Convertis un fichier avec des paramètres personnalisés (le fichier dox_cmd.h dans le code source de assimp liste tous les paramètres disponible) :

`assimp export {{fichier_d_entrée.stl}} {{fichier_de_sortie.obj}} {{paramètres}}`

- Affiche un sommaire du contenu d'un fichier 3D :

`assimp info {{chemin/vers/fichier}}`

- Liste toutes les sous-commandes supportées ("mots") :

`assimp help`

- Affiche l'aide d'un sous-commande (e.g les paramètres qui lui sont spécifique) :

`assimp {{sous_commande}} --help`
