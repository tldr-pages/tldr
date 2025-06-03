# dnf

> Utilitaire de gestion de paquets pour RHEL, Fedora et CentOS (remplace `yum`).
> Certains sous-commandes comme `group` et `config-manager` ont leur propre documentation.
> Pour les commandes équivalentes dans d'autres gestionnaires de paquets, voir : <https://wiki.archlinux.org/title/Pacman/Rosetta>.


- Mettre à jour les paquets installés vers les versions les plus récentes :

`sudo dnf upgrade`

- Rechercher des paquets par mots-clés :

`dnf search {{motclé1 motclé2 ...}}`

- Afficher les détails d’un paquet :

`dnf info {{paquet}}`

- Installer un ou plusieurs paquets (utiliser `-y` pour confirmer automatiquement toutes les invites) :

`sudo dnf install {{paquet1 paquet2 ...}}`

- Supprimer un ou plusieurs paquets :

`sudo dnf remove {{paquet1 paquet2 ...}}`

- Lister les paquets installés :

`dnf list --installed`

- Trouver quels paquets fournissent une commande donnée :

`dnf provides {{commande}}`

- Voir l’historique des opérations effectuées :

`dnf history`
