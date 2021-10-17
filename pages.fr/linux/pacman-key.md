# pacman-key

> Script enrobeur pour GnuPG utilisé pour gérer le trousseau de clés de pacman.
> Plus d'informations : <https://man.archlinux.org/man/community/man-pages-fr/pacman-key.8.fr>.

- Initialiser le trousseau de clés de pacman :

`sudo pacman-key --init`

- Ajouter les clés par défaut pour Arch Linux :

`sudo pacman-key --populate {{archlinux}}`

- Lister les clés publiques du trousseau de clés :

`pacman-key --list-keys`

- Ajouter les clés contenues dans le fichier spécifié :

`sudo pacman-key --add {{chemin/vers/fichier}}`

- Recevoir une clé depuis un serveur de clés :

`sudo pacman-key --recv-keys "{{uid|nom|email}}"`

- Afficher l'empreinte d'une clé du trousseau de clés :

`pacman-key --finger "{{uid|nom|email}}"`

- Signer, localement, une clé du trousseau de clés :

`sudo pacman-key --lsign-key "{{uid|nom|email}}"`

- Supprimer une clé:

`sudo pacman-key --delete "{{uid|nom|email}}"`
