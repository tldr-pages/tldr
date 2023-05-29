# pacman-key

> Script enrobeur pour GnuPG utilisé pour gérer le trousseau de clés de pacman.
> Voir aussi: `pacman`.
> Plus d'informations : <https://man.archlinux.org/man/pacman-key>.

- Initialise le trousseau de clés de pacman :

`sudo pacman-key --init`

- Ajoute les clés par défaut pour Arch Linux :

`sudo pacman-key --populate {{archlinux}}`

- Liste les clés publiques du trousseau de clés :

`pacman-key --list-keys`

- Ajoute les clés contenues dans le fichier spécifié :

`sudo pacman-key --add {{chemin/vers/fichier}}`

- Reçois une clé depuis un serveur de clés :

`sudo pacman-key --recv-keys "{{uid|nom|email}}"`

- Affiche l'empreinte d'une clé du trousseau de clés :

`pacman-key --finger "{{uid|nom|email}}"`

- Signe, localement, une clé du trousseau de clés :

`sudo pacman-key --lsign-key "{{uid|nom|email}}"`

- Supprime une clé :

`sudo pacman-key --delete "{{uid|nom|email}}"`
