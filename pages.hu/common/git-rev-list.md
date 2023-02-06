# git rev-list

> Revíziók (commitok) listázása fordított időrendi sorrendben. További információ: <https://git-scm.com/docs/git-rev-list>.

- Az aktuális ág összes commitjának listázása:

`git rev-list {{HEAD}}`

- Az aktuális ágban egy adott fájlt módosító (hozzáadó/módosító/eltávolító) legutóbbi commit kiírása:

`git rev-list -n 1 HEAD -- {{path/to/file}}`

- Egy adott ágon egy adott dátumnál frissebb commitok listázása:

`git rev-list --since={{'2019-12-01 00:00:00'}} {{branch_name}}`

- Az összes egyesített commit listázása egy adott commiton:

`git rev-list --merges {{commit}}`

- Egy adott címke óta történt commitok számának kiírása:

`git rev-list {{tag_name}}..HEAD --count`
