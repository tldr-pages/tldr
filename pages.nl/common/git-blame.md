# git blame

> Toon welke commit en auteur een bestand voor het laatst heeft gewijzigd.
> Meer informatie: <https://git-scm.com/docs/git-blame>.

- Toon een bestand met informatie over de auteur (auteursnaam en commithash):

`git blame {{pad/naar/bestand}}`

- Toon de e-mail van de auteur in plaats van de naam:

`git blame {{[-e|--show-email]}} {{pad/naar/bestand}}`

- Toon bestand met auteursnaam en commit hash op elke regel op een specifieke commit:

`git blame {{commit}} {{pad/naar/bestand}}`

- Toon bestand met auteursnaam en commit hash op elke regel vóór een specifieke commit:

`git blame {{commit}}~ {{pad/naar/bestand}}`

- Toon een bestand met informatie over de auteur, begginend bij een gegeven regel:

`git blame -L {{123}} {{pad/naar/bestand}}`

- Toon auteursnaam en commit hash informatie voor een specifieke regelbereik:

`git blame -L {{start_regel}},{{eind_regel}} {{pad/naar/bestand}}`

- Annoteer 10 regels van een bestand, beginnend bij de eerste regel die overeenkomt met een gegeven tekenreeks:

`git blame -L '/{{tekst}}/',+10 {{pad/naar/bestand}}`

- Annoteer een bestand zonder witruimtes en regelverplaatsingen:

`git blame -w -C -C -C {{pad/naar/bestand}}`
