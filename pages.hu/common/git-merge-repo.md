# git merge-repo

> Két repository történetének egyesítése. A `git-extras` része. További információ: [https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo.](https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo)

- Egy adattár ágának egyesítése az aktuális adattár könyvtárába:

`git merge-repo {{path/to/repo}} {{branch_name}} {{path/to/directory}}`

- Egy távoli tároló ágának beolvasztása az aktuális tároló könyvtárába, az előzmények megőrzése nélkül:

`git merge-repo {{path/to/remote_repo}} {{branch_name}} .`
