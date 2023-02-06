# git apply

> Foltok alkalmazása a fájlokra és/vagy az indexre. További információ: <https://git-scm.com/docs/git-apply>.

- Üzenetek nyomtatása a javított fájlokról:

`git apply --verbose {{path/to/file}}`

- Alkalmazza és hozzáadja a javított fájlokat az indexhez:

`git apply --index {{path/to/file}}`

- Távoli javítófájl alkalmazása:

`curl {{https://example.com/file.patch}} | git apply`

- Diffstat kimenete a bemenethez és a javítás alkalmazása:

`git apply --stat --apply {{path/to/file}}`

- Alkalmazza a javítást fordítva:

`git apply --reverse {{path/to/file}}`

- A javítás eredményének tárolása az indexben a munkafa módosítása nélkül:

`git apply --cache {{path/to/file}}`
