# basename

> Retourne la portion ne contenant pas de dossiers d'un chemin complet.
> Plus d'informations : <https://man7.org/linux/man-pages/man1/basename.1.html>.

- N'afficher que le nom du fichier depuis un chemin :

`basename {{chemin/vers/fichier}}`
- N'afficher que le nom du dernier répertoire depuis un chemin :

`basename {{chemin/vers/répertoire/}}`

- N'afficher que le nom du fichier depuis un chemin, en ôtant un préfixe donné :

`basename {{chemin/vers/fichier}} {{suffixe}}`
