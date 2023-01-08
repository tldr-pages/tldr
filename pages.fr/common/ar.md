# ar

> Crée, modifie et extrais depuis des archives (`.a`, `.so`, `.o`).
> Plus d'informations : <https://manned.org/ar>.

- Extrais tous les éléments depuis une archive :

`ar -x {{chemin/vers/archive.a}}`

- Liste tous les éléments depuis une archive :

`ar -t {{chemin/vers/archive.a}}`

- Remplace ou ajoute des fichiers à une archive :

`ar -r {{chemin/vers/archive.a}} {{chemin/vers/fichier1.o}} {{chemin/vers/fichier2.o}}`

- Insère un fichier d'indexation (équivalent à `ranlib`) :

`ar -s {{chemin/vers/archive.a}}`

- Crée une archive avec des fichiers et un fichier d'indexation qui l'accompagne :

`ar -rs {{chemin/vers/archive.a}} {{chemin/vers/fichier1.o}} {{chemin/vers/fichier2.o}}`
