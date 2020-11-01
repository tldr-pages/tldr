# git update-index

> Commande git pour manipuler l'index.
> Plus d'informations: <https://git-scm.com/docs/git-update-index>.

- Prétendre qu'un fichier modifié est inchangé (`git status` ne l'affichera pas comme modifié):

`git update-index --skip-worktree {{chemin/vers/fichier_modifié}}`
