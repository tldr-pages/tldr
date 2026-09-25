# nvm

> Installeer, deïnstalleer of wissel tussen verschillende Node.js-versies.
> Ondersteunt versienummers zoals "12.8" of "v16.13.1", en labels zoals "node", "system", enz.
> Zie ook: `asdf`.
> Meer informatie: <https://github.com/nvm-sh/nvm#usage>.

- Installeer/verwijder een specifieke versie van Node.js:

`nvm {{install|uninstall}} {{node_versie}}`

- Gebruik een specifieke versie van Node.js in de huidige shell:

`nvm use {{node_versie}}`

- Stel de standaardversie van Node.js in:

`nvm alias default {{node_versie}}`

- Toon externe versies beschikbaar voor installeren, waarbij alleen LTS (long-term support) versies worden getoond:

`nvm ls-remote --lts`

- Toon geïnstalleerde versies:

`nvm {{[ls|list]}}`

- Start de REPL van een specifieke versie van Node.js:

`nvm run {{node_versie}}`

- Voer een script uit in een specifieke versie van Node.js:

`nvm exec {{node_versie}} node {{pad/naar/script.js}}`

- Upgrade naar de nieuwste werkende npm-versie op de huidige Node.js-versie:

`nvm install-latest-npm`
