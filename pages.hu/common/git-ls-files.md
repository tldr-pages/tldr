# git ls-files

> Az indexben és a munkafában lévő fájlokra vonatkozó információk megjelenítése. További információ: <https://git-scm.com/docs/git-ls-files>.

- Törölt fájlok megjelenítése:

`git ls-files --deleted`

- Módosított és törölt fájlok megjelenítése:

`git ls-files --modified`

- Figyelmen kívül hagyott és nem követett fájlok megjelenítése:

`git ls-files --others`

- Nyomon nem követett, nem figyelmen kívül hagyott fájlok megjelenítése:

`git ls-files --others --exclude-standard`
