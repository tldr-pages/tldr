# tsc

> compilator TypeScript.
> Mai multe informaţii: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>

- Compilați un fișier TypeScript `foobar.ts` într-un fișier JavaScript `foobar.js`:

`tsc {{foobar.ts}}`

- Compilați un fișier TypeScript în JavaScript utilizând o sintaxă țintă specifică (implicit este `ES3`):

`tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foobar.ts}}`

- Compilați un fișier TypeScript într-un fișier JavaScript cu un nume personalizat:

`tsc --outFile {{output.js}} {{input.ts}}`

- Compilează toate fișierele `.ts` ale unui proiect TypeScript definit într-un fișier `tsconfig.json`:

`tsc --build {{tsconfig.json}}`

- Rulați compilatorul utilizând opțiunile de linie de comandă și argumentele preluate dintr-un fișier text:

`tsc @{{args.txt}}`

- Verificați mai multe fișiere JavaScript și ieșiți numai erorile:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`
