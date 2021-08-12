# ts-node

> Rulați codul TypeScript direct, fără nicio compilare.
> Mai multe informaţii: <https://www.npmjs.com/package/ts-node>

- Execută un fișier TypeScript fără compilare (`node` + `tsc`):

`ts-node {{path/to/file.ts}}`

- Executa un fisier TypeScript fara a incarca `tsconfig.json`:

`ts-node --skip-project {{path/to/file.ts}}`

- Evaluați codul TypeScript trecut ca literal pe linia de comandă:

`ts-node --eval '{{console.log("Hello World")}}'`

- Executați un fișier TypeScript în modul script:

`ts-node --script-mode {{path/to/file.ts}}`

- Transpile un fișier TypeScript în JavaScript fără a executa:

`ts-node --transpile-only {{path/to/file.ts}}`

- Afișează ajutorul TS-nod:

`ts-node --help`
