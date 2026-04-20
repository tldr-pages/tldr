# astyle

> Indente, formate, et embelli du code source pour des languages de programmation comme C, C++, C# et Java.
> Pendant l'exécution, une copie du fichier original est créé avec un ".orig" suffixé au nom de fichier original.
> Plus d'informations : <https://manned.org/astyle>.

- Applique le style par défaut de 4 espaces pour l'indentation et pas de changement de formatage :

`astyle {{fichier_source}}`

- Applique le style Java avec le style `attached` :

`astyle {{[-A2|--style=java]}} {{chemin/vers/fichier}}`

- Applique le style `allman` :

`astyle {{[-A1|--style=allman]}} {{chemin/vers/fichier}}`

- Applique une indentation personnalisé avec des espaces. Choisi entre 2 et 20 espaces :

`astyle {{[-s|--indent=spaces=]}}{{nombre_d_espaces}} {{chemin/vers/fichier}}`

- Applique une indentation personnalisé avec des tabulations. Choisi entre 2 et 20 tabulations :

`astyle {{[-t|--indent=tab=]}}{{nombre_de_tabulations}} {{chemin/vers/fichier}}`
