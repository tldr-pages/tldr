# gcc

> Préprocesse et compile des fichiers sources C et C++, pour ensuite les assembler et les lier entre eux.
> Plus d'informations : <https://gcc.gnu.org>

- Compile plusieurs fichiers source en un exécutable :

`gcc {{chemin/vers/le/fichier1.c chemin/vers/le/fichier2.c ...}} -o {{chemin/vers/l'exécutable/à/produire}}`

- Active les averissements et les symboles de débogage dans la sortie de commande :

`gcc {{chemin/vers/le/fichiersource.c}} -Wall -Og -o {{chemin/vers/l'exécutable/à/produire}}`

- Inclut les bibliothèques depuis un chemin différent de celui par défaut :

`gcc {{chemin/vers/le/fichiersource.c}} -o {{chemin/vers/l'exécutable/à/produire}} -I{{chemin/vers/les/fichiers/d'en-tête}} -L{{chemin/vers/la/bibliothèque}} -l{{bibliothèque}}`

- Compile le code source en des instructions d'assemblage :

`gcc -S {{chemin/vers/le/fichiersource.c}}`

- Compile le code source en un fichier objet sans le lier :

`gcc -c {{chemin/vers/le/fichiersource.c}}`
