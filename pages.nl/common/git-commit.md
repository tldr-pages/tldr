# git commit

> Commit bestanden en veranderingen naar de repository.
> Meer informatie: <https://git-scm.com/docs/git-commit>.

- Commit gestagede bestanden (dit opent een venster):

`git commit`

- Commit gestagede bestanden naar de repository met een bericht:

`git commit -m "{{bericht}}"`

- Commit gestagede bestanden met een bericht uit een bestand:

`git commit --file {{pad/naar/bestand_met_commit_bericht}}`

- Stage automatisch alle veranderde bestanden en commit met een bericht:

`git commit -a -m "{{bericht}}"`

- Commit gestagede bestanden en onderteken hen met de geconfigureerde GPG sleutel:

`git commit -S -m "{{bericht}}"`

- Update de laatste commit en voeg nieuwe gestagede veranderingen toe:

`git commit --amend`

- Commit enkel specifieke (al gestagede) bestanden:

`git commit {{pad/naar/bestand-1}} {{pad/naar/bestand-2}}`

- Maak een commit, ook al zijn er geen gestagede veranderingen:

`git commit -m "{{bericht}}" --allow-empty`
