# git update-index

> Git parancs az index manipulálására. További információ: <https://git-scm.com/docs/git-update-index>.

- Tegyünk úgy, mintha egy módosított fájl változatlan lenne (`git status` nem fogja ezt megváltoztatottnak mutatni):

`git update-index --skip-worktree {{path/to/modified_file}}`
