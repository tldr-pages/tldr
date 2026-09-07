# btrfs

> Système de fichiers basé sur le principe de copie à l’écriture ("copy-on-write", souvent désigné par son sigle anglais COW) pour Linux.
> Certaines sous-commandes comme `device` ont leur propre documentation.
> Plus d'informations : <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Crée un sous-volume :

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{chemin/vers/sous_volume}}`

- Liste les sous-volumes :

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{chemin/vers/point_de_montage}}`

- Affiche les informations d'utilisation d'espace :

`sudo btrfs {{[f|filesystem]}} df {{chemin/vers/point_de_montage}}`

- Active les quotas :

`sudo btrfs {{[qu|quota]}} {{[e|enable]}} {{chemin/vers/sous_volume}}`

- Affiche les quotas :

`sudo btrfs {{[qg|qgroup]}} {{[s|show]}} {{chemin/vers/sous_volume}}`
