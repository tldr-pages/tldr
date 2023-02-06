# git svn

> Kétirányú működés egy Subversion tároló és a Git között. További információ: <https://git-scm.com/docs/git-svn>.

- SVN tárolóhely klónozása:

`git svn clone {{https://example.com/subversion_repo}} {{local_dir}}`

- Egy SVN-tár klónozása egy adott revíziós számmal kezdődően:

`git svn clone -r{{1234}}:HEAD {{https://svn.example.net/subversion/repo}} {{local_dir}}`

- Helyi klón frissítése a távoli SVN-tárból:

`git svn rebase`

- Frissítések lekérése a távoli SVN-tárból a Git HEAD módosítása nélkül:

`git svn fetch`

- Visszacsatolás az SVN-tárba:

`git svn dcommit`
