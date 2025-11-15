# git switch

> Wissel tussen Git branches. Vereist Git-versie 2.23+.
> Zie ook: `git checkout`.
> Meer informatie: <https://git-scm.com/docs/git-switch>.

- Wissel naar een bestaande branch:

`git switch {{branch_naam}}`

- Creëer een nieuwe branch en wissel ernaar:

`git switch {{[-c|--create]}} {{branch_naam}}`

- Creëer een nieuwe branch gebaseerd op een bestaande commit en wissel ernaar:

`git switch {{[-c|--create]}} {{branch_naam}} {{commit}}`

- Wissel naar de vorige branch:

`git switch -`

- Wissel naar een branch en update alle submodules zodat ze overeenkomen:

`git switch --recurse-submodules {{branch_naam}}`

- Wissel naar een branch en voeg automatisch de huidige branch en alle niet-vastgelegde aanpassingen hierin samen:

`git switch {{[-m|--merge]}} {{branch_naam}}`

- Wissel naar een tag:

`git switch {{[-d|--detach]}} {{tag}}`
