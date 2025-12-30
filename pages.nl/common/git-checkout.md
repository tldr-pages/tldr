# git checkout

> Haal een branch of paden naar de worktree op.
> Meer informatie: <https://git-scm.com/docs/git-checkout>.

- Creëer en schakel naar een nieuwe branch:

`git checkout -b {{branch_naam}}`

- Creëer en schakel naar een nieuwe branch gebaseerd op een specifieke referentie (branch, remote/branch, tag zijn voorbeelden van geldige referenties):

`git checkout -b {{branch_naam}} {{referentie}}`

- Schakel over naar een bestaande lokale branch:

`git checkout {{branch_naam}}`

- Schakel over naar de eerder uitgecheckte branch:

`git checkout -`

- Schakel over naar een bestaande remote branch:

`git checkout {{[-t|--track]}} {{remote_naam}}/{{branch_naam}}`

- Verwijder alle niet-toegevoegde wijzigingen in de huidige map (zie `git reset` voor meer ongedaan maken-achtige commando's):

`git checkout .`

- Verwijder niet-toegevoegde wijzigingen aan een bepaald bestand:

`git checkout {{pad/naar/bestand}}`

- Vervang een bestand in de huidige map door de versie die in een specifieke branch is vastgelegd:

`git checkout {{branch_naam}} -- {{pad/naar/bestand}}`
