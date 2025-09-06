# git

> Gedistribueerd versiebeheersysteem.
> Sommige subcommando's zoals `commit`, `add`, `branch`, `switch`, `push`, etc. hebben hun eigen documentatie.
> Meer informatie: <https://git-scm.com/docs/git>.

- Creëer een lege Git repository:

`git init`

- Kloon een externe Git repository vanaf het internet:

`git clone {{https://example.com/repo.git}}`

- Toon de status van de lokale repository:

`git status`

- Voeg alle veranderingen toe aan een commit:

`git add {{[-A|--all]}}`

- Commit veranderingen naar de versiegeschiedenis:

`git commit {{[-m|--message]}} {{bericht_tekst}}`

- Push lokale commits naar een externe repository:

`git push`

- Haal alle veranderingen op van een externe repository:

`git pull`

- Stel alles opnieuw in zoals het was in de laatste commit:

`git reset --hard; git clean {{[-f|--force]}}`
