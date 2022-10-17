# zypper

> SUSE & openSUSE utilitaire de gestion de paquets.
> Plus d'informations : <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchroniser la liste des paquets et versions disponibles :

`zypper refresh`

- Installer un nouveau paquet :

`zypper install {{paquet}}`

- Supprimer un paquet :

`zypper remove {{paquet}}`

- Mettre à jour un paquet installé vers la version la plus récente disponible :

`zypper update`

- Chercher un paquet par mot clef :

`zypper search {{mot_clef}}`

- Afficher les informations concernant les dépôts de paquets configurés :

`zypper repos --sort-by-priority`
