# ruff check

> Een extreem snelle Python linter. `check` is het standaard commando - het kan overal weggelaten worden.
> Als geen bestanden of mappen zijn gespecificeerd, wordt de huidige map gebruikt.
> Meer informatie: <https://docs.astral.sh/ruff/linter>.

- Voer de linter uit op de opgegeven bestanden of mappen:

`ruff check {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Voer de gesuggereerde fixes uit en pas de bestanden in-place aan:

`ruff check --fix`

- Voer de linter uit en re-lint op iedere wijziging:

`ruff check --watch`

- Zet alleen de gespecificeerde regels (of alle regels) aan en negeer het configuratie bestand:

`ruff check --select {{ALL|regelcode1,regelcode2,...}}`

- Zet additioneel de gespecificeerde regels aan:

`ruff check --extend-select {{regelcode1,regelcode2,...}}`

- Zet de gespecificeerde regels uit:

`ruff check --ignore {{regelcode1,regelcode2,...}}`

- Negeer alle bestaande schendingen van een regel door `# noqa` toe te voegen aan alle regels die de regel breken:

`ruff check --select {{regelcode}} --add-noqa`
