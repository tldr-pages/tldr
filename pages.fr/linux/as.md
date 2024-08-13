# as

> Assembleur GNU portable. Principalement destiné pour assembler la sortie de `gcc` pour être utilisé par `ld`.
> Plus d'informations : <https://manned.org/as>.

- Assemble un fichier, en écrivant la sortie dans le fichier `a.out` :

`as {{chemin/vers/fichier.s}}`

- Assemble la sortie vers un fichier donné :

`as {{chemin/vers/fichier.s}} -o {{chemin/vers/sortie.o}}`

- Génère la sortie plus vite en évitant le preprocess des espaces et des commentaires (doit seulement être utilisé sur des compilateurs sûrs) :

`as -f {{chemin/vers/fichier.s}}`

- Inclut un chemin donné à la liste des répertoires dans lesquels chercher les fichiers spécifiés dans les directives `.include` :

`as -I {{chemin/vers/le/répertoire}} {{chemin/vers/fichier.s}}`
