# git push

> Távoli tárolóhelyre történő commitok átvitele. További információ: <https://git-scm.com/docs/git-push>.

- Az aktuális ág helyi módosításainak elküldése az alapértelmezett távoli megfelelőjének:

`git push`

- Egy adott helyi ág módosításainak elküldése a távoli megfelelőjének:

`git push {{remote_name}} {{local_branch}}`

- Egy adott helyi ág változtatásainak elküldése a távoli megfelelőjébe, és a távoli ág beállítása a helyi ág alapértelmezett push/pull célpontjaként:

`git push -u {{remote_name}} {{local_branch}}`

- Változások küldése egy adott helyi ágból egy adott távoli ágba:

`git push {{remote_name}} {{local_branch}}:{{remote_branch}}`

- Az összes helyi ág változásainak elküldése az adott távoli tárolóhelyen lévő megfelelőiknek:

`git push --all {{remote_name}}`

- Egy távoli adattárban lévő ág törlése:

`git push {{remote_name}} --delete {{remote_branch}}`

- Azon távoli ágak eltávolítása, amelyeknek nincs helyi megfelelője:

`git push --prune {{remote_name}}`

- Olyan címkék közzététele, amelyek még nincsenek a távoli tárolóban:

`git push --tags`
