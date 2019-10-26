# git pull

> Récupère une branche depuis le serveur distant et fusionne  la dans le serveur local
> Plus d'informations : <https://git-scm.com/docs/git-pull>.

- Télécharge les changements depuis le serveur distant par défaut et fusionne les :

`git pull`

- Télécharge les changements depuis le serveur distant par défaut et applique les changements locaux par dessus :

`git pull --rebase`

- Télécharge les changements depuis depuis un serveur et une branche distante, puis fusionne les dans HEAD :

`git pull {{remote_name}} {{branch}}`
