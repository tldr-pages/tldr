# git lfs

> Travailler dans un registre Git avec des fichiers volumineux.
> Plus d'informations : <https://github.com/git-lfs/git-lfs/tree/main/docs>.

- Initialise le Git LFS :

`git lfs install`

- Suit des fichiers correspondant à un pattern :

`git lfs track '{{*.bin}}'`

- Change l'URL du point de terminaison Git LFS (utile si le serveur LFS est séparé du serveur Git) :

`git config {{[-f|--file]}} .lfsconfig lfs.url {{lfs_endpoint_url}}`

- Liste les pattern de fichiers suivis :

`git lfs track`

- Liste les fichiers suivis ayant été commité :

`git lfs ls-files`

- Pousse tout les objets LFS vers le serveur distant :

`git lfs push --all {{nom_distant}} {{nom_de_branche}}`

- Cherche tout les objets LFS :

`git lfs fetch`

- Charge tout les objets LFS :

`git lfs checkout`
