# git rev-list

> Lista revizuirilor (angajări) în ordine cronologică inversă.
> Mai multe informaţii: <https://git-scm.com/docs/git-rev-list>

- Listează toate angajările pe sucursala curentă:

`git rev-list {{HEAD}}`

- Lista se angajează mai recent decât o anumită dată, pe o anumită sucursală:

`git rev-list --since={{'2019-12-01 00:00:00'}} {{branch_name}}`

- Listează toate comite de îmbinare pe un anumit angajament:

`git rev-list --merges {{commit}}`
