# pacman --sync

> Synchronise les paquets depuis les dépôts distants.
> Plus d'informations : <https://manned.org/pacman.8>.

- Installe un nouveau paquet :

`sudo pacman -S {{paquet}}`

- Synchronise et actualise la base de données des paquets en effectuant aussi une mise à niveau du système (ajouter `--downloadonly` pour télécharger uniquement les paquets sans les mettre à jour) :` :

`sudo pacman -Syu`

- Synchronise, met à jour et installe un paquet sans demander de confirmation :

`sudo pacman -Syu --noconfirm {{paquet}}`

- Recherche un paquet en utilisant un mot-clé ou une `regex` :

`pacman -Ss "{{motif_recherche}}"`

- Affiche des informations sur un paquet :

`pacman -Si {{paquet}}`

- Ecrit par-dessus des fichiers en conflit pendant une mise à jour :

`sudo pacman -Syu --overwrite {{chemin/vers/fichier}}`

- Supprime les fichiers concernant des paquets non installés et les dépôts inutilisés du cache de pacman (utiliser les options `Scc` pour nettoyer tous les paquets):

`sudo pacman -Sc`

- Spécifie la version du paquet à installer :

`sudo pacman -S {{paquet}}={{version}}`
