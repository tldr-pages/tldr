# crystal

> Outil de gestion du code source de Crystal.
> Plus d'informations : <https://crystal-lang.org/reference/using_the_compiler>.

- Exécute un fichier Crystal :

`crystal {{chemin/vers/fichier.cr}}`

- Compile un fichier et toutes ses dépendances en un seul exécutable :

`crystal build {{chemin/vers/fichier.cr}}`

- Lit le code source Crystal à partir de la ligne de commande ou de `stdin`, et l'exécute :

`crystal eval '{{code}}'`

- Génère la documentation de l'API à partir commentaires dans les fichiers Crystal :

`crystal docs`

- Compile et exécute une suite de spécifications Crystal :

`crystal spec`

- Démarre un serveur interactif local pour tester le langage :

`crystal play`

- Crée un répertoire de projet pour une application Crystal :

`crystal init app {{nom_application}}`

- Affiche toutes les options d'aide :

`crystal help`
