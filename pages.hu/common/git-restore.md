# git restore

> A munkafa fájljainak visszaállítása. A Git 2.23+ verziója szükséges. Lásd még: `git checkout` és `git reset`. További információ: <https://git-scm.com/docs/git-restore>.

- Visszaállít egy még nem állított fájlt az aktuális commit verziójára (HEAD):

`git restore {{path/to/file}}`

- Visszaállít egy nem állított fájlt egy adott commit verziójára:

`git restore --source {{commit}} {{path/to/file}}`

- A nyomon követett fájlok összes, még el nem végzett módosításának elvetése:

`git restore :/`

- Egy fájl stádiumának feloldása:

`git restore --staged {{path/to/file}}`

- Az összes fájl törlése:

`git restore --staged :/`

- Az összes módosítás elvetése a fájlokon, mind a szakaszolt, mind a szakaszolatlan fájlokon:

`git restore --worktree --staged :/`

- A visszaállítandó fájlok szakaszainak interaktív kiválasztása:

`git restore --patch`
