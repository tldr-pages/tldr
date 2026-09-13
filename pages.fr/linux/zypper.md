# zypper

> SUSE & openSUSE utilitaire de gestion de paquets.
> Pour les commandes équivalentes dans d’autres gestionnaires de paquets, consulter <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Plus d'informations : <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronise la liste des paquets et versions disponibles :

`sudo zypper {{[ref|refresh]}}`

- Installe un nouveau paquet :

`sudo zypper {{[in|install]}} {{paquet}}`

- Supprime un paquet :

`sudo zypper {{[rm|remove]}} {{paquet}}`

- Met à jour un paquet installé vers la version la plus récente disponible :

`sudo zypper {{[up|update]}}`

- Réalise une mise à niveau de la distribution :

`sudo zypper {{[dup|dist-upgrade]}}`

- Cherche un paquet par mot clef :

`zypper {{[se|search]}} {{mot_clef}}`

- Affiche les informations concernant les dépôts de paquets configurés :

`zypper {{[lr|repos]}} --sort-by-priority`
