# git svn

> Operațiune bidirecțională între un depozit Subversion și Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-svn>

- Clonează un depozit SVN:

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- Clonează un depozit SVN începând de la un anumit număr de revizuire:

`git svn clone -r{{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- Actualizați clona locală din depozitul SVN la distanță:

`git svn rebase`

- Obțineți actualizări din depozitul SVN la distanță fără a schimba Git HEAD:

`git svn fetch`

- Reveniți la depozitul SVN:

`git svn dcommit`
