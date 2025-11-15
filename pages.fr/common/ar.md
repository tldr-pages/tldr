# ar

> Crée, modifie et extrais depuis des archives (`.a`, `.so`, `.o`).
> Plus d'informations : <https://manned.org/ar>.

- E[x]trais tous les éléments depuis une archive :

`ar x {{chemin/vers/archive.a}}`

- Lis[t]e tous les éléments depuis une archive :

`ar t {{chemin/vers/archive.ar}}`

- [r]emplace ou ajoute des fichiers à une archive :

`ar r {{chemin/vers/archive.deb}} {{chemin/vers/debian-binary chemin/vers/control.tar.gz chemin/vers/data.tar.xz ...}}`

- In[s]ère un fichier d'indexation (équivalent à `ranlib`) :

`ar s {{chemin/vers/archive.a}}`

- Crée une archive avec des fichiers et un fichier d'indexation qui l'accompagne :

`ar rs {{chemin/vers/archive.a}} {{chemin/vers/fichier1.o chemin/vers/fichier2.o ...}}`
