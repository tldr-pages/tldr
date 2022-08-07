# astyle

> Indente, formate, et embelli du code source pour des languages de programmation comme C, C++, C# et Java.
> Pendant l'exécution, une copie du fichier original est créé avec un ".orig" suffixé au nom de fichier original.
> Plus d'informations : <http://astyle.sourceforge.net/>.

- Applique le style par défaut de 4 espaces pour l'indentation et pas de changement de formatage :

`astyle {{fichier_source}}`

- Applique le style Java avec le style `attached` :

`astyle --style=java {{chemin/vers/fichier}}`

- Applique le style `allman` :

`astyle --style=allman {{chemin/vers/fichier}}`

- Applique une indentation personnalisé avec des espaces. Choisi entre 2 et 20 espaces :

`astyle --indent=spaces={{nombre_d_espaces}} {{chemin/vers/fichier}}`

- Applique une indentation personnalisé avec des tabulations. Choisi entre 2 et 20 tabulations :

`astyle --indent=tab={{nombre_de_tabulations}} {{chemin/vers/fichier}}`
