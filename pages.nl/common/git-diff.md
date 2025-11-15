# git diff

> Toon veranderingen in bijgehouden bestanden.
> Meer informatie: <https://git-scm.com/docs/git-diff>.

- Toon niet-toegevoegde veranderingen:

`git diff`

- Toon alle niet-gecommitte (inclusief de toegevoegde) veranderingen:

`git diff HEAD`

- Toon alleen toegevoegde (nog niet gecommitte) veranderingen:

`git diff --staged`

- Toon veranderingen van alle commits sinds een bepaalde datum/tijd (een datumexpressie, b.v. "1 week 2 days" of een ISO-datum):

`git diff 'HEAD@{{{3 months|weeks|days|hours|seconds ago}}}'`

- Toon diff-statistieken, zoals gewijzigde bestanden, histogram en het totale aantal ingevoegde/verwijderde regels:

`git diff --stat {{commit}}`

- Toon een samenvatting van aangemaakte bestanden, hernoemingen en moduswijzigingen sinds een bepaalde commit:

`git diff --summary {{commit}}`

- Vergelijk een bestand tussen twee branches of commits:

`git diff {{branch_1}}..{{branch_2}} {{pad/naar/bestand}}`

- Vergelijk verschillende bestanden van de huidige branch met een andere branch:

`git diff {{andere_branch}}:{{pad/naar/bestand2}} {{pad/naar/bestand1}}`
