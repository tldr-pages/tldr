# zypper

> SUSE & openSUSE utilitaire de gestion de paquets.
> Plus d'informations : <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchroniser la liste des paquets et versions disponibles :

`sudo zypper {{[ref|refresh]}}`

- Installer un nouveau paquet :

`sudo zypper {{[in|install]}} {{paquet}}`

- Supprimer un paquet :

`sudo zypper {{[rm|remove]}} {{paquet}}`

- Mettre à jour un paquet installé vers la version la plus récente disponible :

`sudo zypper {{[up|update]}}`

- Chercher un paquet par mot clef :

`zypper {{[se|search]}} {{mot_clef}}`

- Afficher les informations concernant les dépôts de paquets configurés :

`zypper {{[lr|repos]}} --sort-by-priority`
