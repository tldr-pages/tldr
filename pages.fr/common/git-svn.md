# git svn

> Opération bidirectionnelle entre un référentiel Subversion et Git.
> Plus d'informations : <https://git-scm.com/docs/git-svn>.

- Clone un dépôt SVN :

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- Clone un dépôt SVN à partir d'une révision donnée :

`git svn clone {{[-r|--revision]}} {{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- Met à jour le clone local à partir du dépôt SVN distant :

`git svn rebase`

- Cherche les changements distants dans le dépôt SVN sans les appliquer sur le HEAD :

`git svn fetch`

- Valide sur le SVN :

`git svn commit`
