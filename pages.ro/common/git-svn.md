# git svn

> Operație bidirecțională între un repository Subversion și Git.
> Mai multe informații: <https://git-scm.com/docs/git-svn>.

- Clonează un repository SVN:

`git svn clone {{https://example.com/subversion_repo}} {{director_local}}`

- Clonează un repository SVN pornind de la un număr de revizie dat:

`git svn clone {{[-r|--revision]}} {{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{director_local}}`

- Actualizează clona locală din repository-ul SVN la distanță:

`git svn rebase`

- Preia actualizări din repository-ul SVN la distanță fără a schimba `HEAD`-ul Git:

`git svn fetch`

- Confirmă înapoi în repository-ul SVN:

`git svn commit`
