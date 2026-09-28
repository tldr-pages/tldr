# choco new

> Génère de nouveaux fichiers de spécifications de package avec Chocolatey.
> Plus d'informations : <https://docs.chocolatey.org/en-us/create/commands/new/>.

- Crée un nouveau squelette de package :

`choco new {{paquet}}`

- Crée un nouveau package avec une version spécifique :

`choco new {{paquet}} --version {{version}}`

- Crée un nouveau package avec un nom de responsable spécifique :

`choco new {{paquet}} --maintainer {{nom_mainteneur}}`

- Crée un nouveau package dans un répertoire de sortie personnalisé :

`choco new {{paquet}} {{[--out|--output-directory]}} {{chemin/vers/repertoire}}`

- Crée un nouveau package avec des URL d'installation 32 bits et 64 bits spécifiques :

`choco new {{paquet}} url="{{url}}" url64="{{url}}"`
