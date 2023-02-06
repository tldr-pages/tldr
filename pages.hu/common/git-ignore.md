# git ignore

> A `.gitignore` fájlok megjelenítése/frissítése. A `git-extras` része. Lásd még: `git ignore-io`. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>.

- Az összes globális és helyi `.gitignore` fájl tartalmának megjelenítése:

`git ignore`

- A fájl(ok) privát figyelmen kívül hagyása, a `.git/info/exclude` fájl frissítése:

`git ignore {{file_pattern}} --private`

- Helyi fájl(ok) figyelmen kívül hagyása, helyi `.gitignore` fájl frissítése:

`git ignore {{file_pattern}}`

- Globális fájl(ok) figyelmen kívül hagyása, globális `.gitignore` fájl frissítése:

`git ignore {{file_pattern}} --global`
