# git summary

> Egy Git-tárhelyről szóló információk megjelenítése. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>.

- Adatok megjelenítése egy Git-tárhelyről:

`git summary`

- Egy Git-tárhelyre vonatkozó adatok megjelenítése egy commit-olás óta:

`git summary {{commit|branch_name|tag_name}}`

- Adatok megjelenítése egy Git-tárról, a különböző e-maileket használó committerek összevonása 1 statisztikába minden szerző számára:

`git summary --dedup-by-email`

- Adatok megjelenítése egy Git-tárról, az egyes közreműködők által módosított sorok számának megjelenítése:

`git summary --line`
