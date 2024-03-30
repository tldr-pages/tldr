# choco new

> Générez de nouveaux fichiers de spécifications de package avec Chocolatey.
> Plus d'informations : <https://chocolatey.org/docs/commands-new>.

- Créer un nouveau squelette de package :

`choco new {{paquet}}`

- Créer un nouveau package avec une version spécifique :

`choco new {{paquet}} --version {{version}}`

- Créer un nouveau package avec un nom de responsable spécifique :

`choco new {{paquet}} --maintainer {{nom_mainteneur}}`

- Créer un nouveau package dans un répertoire de sortie personnalisé :

`choco new {{paquet}} --output-directory {{chemin/vers/répertoire}}`

- Créez un nouveau package avec des URL d'installation 32 bits et 64 bits spécifiques :

`choco new {{paquet}} url="{{url}}" url64="{{url}}"`
