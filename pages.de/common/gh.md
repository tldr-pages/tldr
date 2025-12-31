# gh

> Arbeite mit GitHub von der Konsole aus.
> Manche Unterbefehle wie `config` sind separat dokumentiert.
> Weitere Informationen: <https://cli.github.com/manual/gh>.

- Klone ein GitHub Repository lokal:

`gh repo clone {{besitzer}}/{{repository}}`

- Erstelle ein neues Issue:

`gh issue {{[new|create]}}`

- Zeige und filter offene Issues des aktuellen Repositories:

`gh issue {{[ls|list]}}`

- Öffne ein Issue im Standard-Webbrowser:

`gh issue view {{[-w|--web]}} {{issue_nummer}}`

- Erstelle eine Pull Request:

`gh pr {{[new|create]}}`

- Öffne eine Pull Request im Standard-Webbrowser:

`gh pr view {{[-w|--web]}} {{pr_nummer}}`

- Wechsle lokal zu einer bestimmten Pull Request:

`gh {{[co|pr checkout]}} {{pr_nummer}}`

- Zeige den Status der Pull Requests eines Repositories:

`gh pr status`
