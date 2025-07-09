# git blame

> Toon commit hash en laatste auteur op elke regel van een bestand.
> Meer informatie: <https://git-scm.com/docs/git-blame>.

- Toon bestand met auteursnaam en commit hash op elke regel:

`git blame {{pad/naar/bestand}}`

- Toon bestand met e-mailadres van de auteur en commit hash op elke regel:

`git blame {{[-e|--show-email]}} {{pad/naar/bestand}}`

- Toon bestand met auteursnaam en commit hash op elke regel op een specifieke commit:

`git blame {{commit}} {{pad/naar/bestand}}`

- Toon bestand met auteursnaam en commit hash op elke regel vóór een specifieke commit:

`git blame {{commit}}~ {{pad/naar/bestand}}`

- Toon auteursnaam en commit hash informatie voor een specifieke regelbereik:

`git blame -L {{start_regel}},{{eind_regel}} {{pad/naar/bestand}}`

- Negeer witruimtes en regelverplaatsingen:

`git blame -w -C -C -C {{pad/naar/bestand}}`
