# git diff

> Geef verandering weer in bijgehouden bestanden.
> Meer informatie: <https://git-scm.com/docs/git-diff>.

- Laat niet-gestagede, ongecommitte veranderingen zien:

`git diff`

- Laat alle ongecommitte veranderingen zien (inclusief gestagede veranderingen):

`git diff HEAD`

- Laat enkel gestagede veranderingen zien (deze zijn toegevoegd maar niet gecommit):

`git diff --staged`

- Laat enkel de namen zien van veranderde bestanden sinds een commit:

`git diff --name-only {{commit}}`

- Geef een overzicht van aangemaakte, hernoemde en mode-veranderde bestanden sinds een commit:

`git diff --summary {{commit}}`

- Vergelijk een bestand tussen twee branches of commits:

`git diff {{branch_1}}..{{branch_2}} [--] {{pad/naar/bestand}}`

- Vergelijk verschillende bestanden van een andere branch met een van de huidige branch:

`git diff {{branch}}:{{pad/naar/bestand-1}} {{pad/naar/bestand-2}}`
