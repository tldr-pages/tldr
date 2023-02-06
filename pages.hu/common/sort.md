# sort

> Szövegfájlok sorainak rendezése. További információ: <https://www.gnu.org/software/coreutils/sort>.

- Fájlok növekvő sorrendbe rendezése:

`sort {{path/to/file}}`

- Fájl rendezése csökkenő sorrendben:

`sort --reverse {{path/to/file}}`

- Fájl rendezése a nagy- és kisbetűket nem figyelembe vevő módon:

`sort --ignore-case {{path/to/file}}`

- Fájl rendezése numerikus, nem pedig betűrendben:

`sort --numeric-sort {{path/to/file}}`

- A `/etc/passwd` oldal rendezése minden sor 3. mezője szerint numerikusan, ":" mezőelválasztóként használva:

`sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}`

- Rendezzen egy fájlt úgy, hogy csak az egyedi sorok maradjanak meg:

`sort --unique {{path/to/file}}`

- Fájl rendezése, a kimenetet a megadott kimeneti fájlba nyomtatva (fájl helyben történő rendezésére is használható):

`sort --output={{path/to/file}} {{path/to/file}}`

- Számok rendezése exponensekkel:

`sort --general-numeric-sort {{path/to/file}}`
