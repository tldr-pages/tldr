# git annotate

> A commit hash és az utolsó szerző megjelenítése egy fájl minden sorában. Lásd: `git blame`, amely előnyben részesül a `git annotate` helyett. A`git annotate` azok számára készült, akik más verziókezelő rendszerekkel ismerkednek. További információ: <https://git-scm.com/docs/git-annotate>.

- Nyomtasson ki egy fájlt úgy, hogy a szerző neve és a commit hash minden egyes sorba be van illesztve:

`git annotate {{path/to/file}}`

- Egy fájl kinyomtatása a szerző e-mail címével és a commit hash-számmal minden sor előtt:

`git annotate -e {{path/to/file}}`
