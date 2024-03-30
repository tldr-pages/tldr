# git svn

> Operazioni bidirezionali tra repository Subversion e Git.
> Maggiori informazioni: <https://git-scm.com/docs/git-svn>.

- Clona un repository SVN:

`git svn clone {{https://esempio.com/repo_subversion}} {{directory_locale}}`

- Clona un repository SVN a partire da uno specifico numero di revisione:

`git svn clone -r{{1234}}:HEAD {{https://svn.esempio.net/subversion/repo}} {{directory_locale}}`

- Aggiorna una copia locale da un repository SVN remoto:

`git svn rebase`

- Scarica aggiornamenti da un repository SVN remoto senza spostare l'HEAD Git:

`git svn fetch`

- Invia un commit a un repository SVN:

`git svn commit`
