# git mv

> Fájlok áthelyezése vagy átnevezése és a Git-index frissítése. További információ: <https://git-scm.com/docs/git-mv>.

- Fájl áthelyezése a repón belül, és a mozgatás hozzáadása a következő commithoz:

`git mv {{path/to/file}} {{new/path/to/file}}`

- Fájl átnevezése és az átnevezés hozzáadása a következő commithoz:

`git mv {{filename}} {{new_filename}}`

- A fájl felülírása a cél elérési útvonalon, ha létezik:

`git mv --force {{file}} {{target}}`
