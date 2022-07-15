# adscript

> Compilateur pour fichiers Adscript.
> Plus d'informations : <https://github.com/Amplus2/Adscript>.

- Compile un fichier vers un fichier objet :

`adscript --output {{chemin/vers/fichier.o}} {{chemin/vers/fichier_source.adscript}}`

- Compile et lie un fichier vers un exécutable autonome :

`adscript --executable --output {{chemin/vers/fichier}} {{chemin/vers/fichier_source.adscript}}`

- Compile un fichier vers LLVM IR à la place du code machine natif :

`adscript --llvm-ir --output {{chemin/vers/fichier.ll}} {{chemin/vers/fichier_source.adscript}}`

- Fait une compilation croisée d'un fichier vers un fichier objet pour une architecture CPU ou un système d'exploitation distant :

`adscript --target-triple {{i386-linux-elf}} --output {{chemin/vers/fichier.o}} {{chemin/vers/fichier_source.adscript}}`
