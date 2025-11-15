# nvm

> Installeer, deïnstalleer of wissel tussen verschillende Node.js-versies.
> Ondersteunt versienummers zoals "12.8" of "v16.13.1", en labels zoals "stable", "system", enz.
> Zie ook: `asdf`.
> Meer informatie: <https://github.com/creationix/nvm>.

- Installeer een specifieke versie van Node.js:

`nvm install {{node_versie}}`

- Gebruik een specifieke versie van Node.js in de huidige shell:

`nvm use {{node_versie}}`

- Stel de standaardversie van Node.js in:

`nvm alias default {{node_versie}}`

- Toon alle beschikbare Node.js-versies en markeer de standaardversie:

`nvm list`

- Deïnstalleer een bepaalde versie van Node.js:

`nvm uninstall {{node_versie}}`

- Start de REPL van een specifieke versie van Node.js:

`nvm run {{node_versie}} --version`

- Voer een script uit in een specifieke versie van Node.js:

`nvm exec {{node_versie}} node {{app.js}}`
