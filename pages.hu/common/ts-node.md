# ts-node

> TypeScript kód futtatása közvetlenül, fordítás nélkül. További információ: <https://typestrong.org/ts-node>.

- TypeScript fájl végrehajtása fordítás nélkül (`node` + `tsc`):

`ts-node {{path/to/file.ts}}`

- TypeScript-fájl végrehajtása betöltés nélkül `tsconfig.json`:

`ts-node --skip-project {{path/to/file.ts}}`

- A parancssoron literálként átadott TypeScript kód kiértékelése:

`ts-node --eval '{{console.log("Hello World")}}'`

- TypeScript fájl végrehajtása script módban:

`ts-node --script-mode {{path/to/file.ts}}`

- TypeScript-fájl átfordítása JavaScript-be végrehajtás nélkül:

`ts-node --transpile-only {{path/to/file.ts}}`

- TS-Node súgó megjelenítése:

`ts-node --help`
