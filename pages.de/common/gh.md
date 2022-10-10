# gh

> Arbeite mit GitHub von der Konsole aus.
> Manche Unterbefehle wie `gh config` sind separat dokumentiert.
> Weitere Informationen: <https://cli.github.com/>.

- Klone ein GitHub Repository lokal:

`gh repo clone {{besitzer}}/{{repository}}`

- Erstelle ein neues Issue:

`gh issue create`

- Zeige und filter offene Issues des aktuellen Repositories:

`gh issue list`

- Öffne ein Issue im Standard-Webbrowser:

`gh issue view --web {{issue_nummer}}`

- Erstelle eine Pull Request:

`gh pr create`

- Öffne eine Pull Request im Standard-Webbrowser:

`gh pr view --web {{pr_nummer}}`

- Wechsle lokal zu einer bestimmten Pull Request:

`gh pr checkout {{pr_nummer}}`

- Zeige den Status der Pull Requests eines Repositories:

`gh pr status`
