# git reset

> Maak commits of niet-toegevoegde wijzigingen ongedaan door de huidige Git HEAD te herstellen naar de opgegeven status.
> Als een pad is opgegeven, werkt dit als "unstage"; als een commit-hash of branch is meegegeven, werkt dit als "uncommit".
> Meer informatie: <https://git-scm.com/docs/git-reset>.

- Maak alle toevoegingen ongedaan:

`git reset`

- Maak toevoegingen van bepaalde bestand(en) ongedaan:

`git reset {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Maak toevoegingen van delen van een bestand interactief ongedaan:

`git reset {{[-p|--patch]}} {{pad/naar/bestand}}`

- Maak de laatste commit ongedaan, waarbij de wijzigingen (en alle andere ongecommitte wijzigingen) in de bestandssysteem blijven:

`git reset HEAD~`

- Maak de laatste twee commits ongedaan en voeg hun veranderingen toe aan de index, d.w.z. toegevoegd voor commit:

`git reset --soft HEAD~2`

- Verwijder alle ongecommitte veranderingen, toegevoegd of niet (voor alleen niet-toegevoegde wijzigingen, gebruik `git checkout`):

`git reset --hard`

- Herstel de repository naar een bepaalde commit, waarbij gecommitte, toegevoegde en niet-gecommite wijzigingen sindsdien worden verwijderd:

`git reset --hard {{commit}}`
