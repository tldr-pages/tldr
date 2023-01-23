# tsc

> TypeScript fordító. További információ: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- Fordítson le egy TypeScript-fájlt `foobar.ts` egy JavaScript-fájllá `foobar.js`:

`tsc {{foobar.ts}}`

- TypeScript fájl fordítása JavaScript-be egy adott célszintaxissal (alapértelmezett: `ES3`):

`tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foobar.ts}}`

- TypeScript-fájl fordítása JavaScript-fájlba egy egyéni névvel:

`tsc --outFile {{output.js}} {{input.ts}}`

- A `tsconfig.json` fájlban definiált TypeScript projekt összes `.ts` fájljának lefordítása:

`tsc --build {{tsconfig.json}}`

- A fordító futtatása parancssori opciók és szöveges fájlból származó argumentumok használatával:

`tsc @{{args.txt}}`

- Több JavaScript-fájl típusellenőrzése, és csak a hibák kimenete:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`
