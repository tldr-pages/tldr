# git svn

> Opération bidirectionnelle entre un référentiel Subversion et Git.
> Plus d'informations : <https://git-scm.com/docs/git-svn>.

- Cloner un dépôt SVN :

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- Cloner un dépôt SVN à partir d'une révision donnée :

`git svn clone -r{{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- Mettre à jour le clone local à partir du dépôt SVN distant :

`git svn rebase`

- Chercher les changements distants dans le dépôt SVN dans les appliquer sur le HEAD :

`git svn fetch`

- Commiter sur le SVN :

`git svn commit`
