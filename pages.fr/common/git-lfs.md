# git lfs

> Travailler dans un registre Git avec des fichiers volumineux.
> Plus d'informations : <https://git-lfs.com>.

- Initialise le Git LFS :

`git lfs install`

- Suivre des fichiers correspondant à un pattern :

`git lfs track '{{*.bin}}'`

- Changer l'URL du point de terminaison Git LFS (utile si le serveur LFS est séparé du serveur Git) :

`git config -f .lfsconfig lfs.url {{lfs_endpoint_url}}`

- Lister les pattern de fichiers suivis :

`git lfs track`

- Lister les fichiers suivis ayant été commité :

`git lfs ls-files`

- Pousser tout les objets LFS vers le serveur distant :

`git lfs push --all {{nom_distant}} {{nom_de_branche}}`

- Chercher tout les objets LFS :

`git lfs fetch`

- Charger tout les objets LFS :

`git lfs checkout`
