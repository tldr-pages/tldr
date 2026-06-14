# tsc

> TypeScript կոմպիլյատոր:.
> Լրացուցիչ տեղեկություններ. <https://www.typescriptlang.org/docs/handbook/compiler-options.html>:.

- Նախաձեռնել TypeScript նախագիծը.:

`tsc --init`

- Կազմեք TypeScript ֆայլը նույն անունով JavaScript ֆայլի մեջ.:

`tsc {{path/to/file.ts}}`

- Կազմեք TypeScript ֆայլը JavaScript-ում՝ օգտագործելով հատուկ թիրախային շարահյուսություն (կանխադրվածը `ES3` է):

`tsc {{[-t|--target]}} {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT|...}} {{path/to/file.ts}}`

- Կազմեք TypeScript ֆայլը JavaScript ֆայլի մեջ հատուկ անունով.:

`tsc --outFile {{path/to/output_file.js}} {{path/to/input_file.ts}}`

- Կազմեք TypeScript նախագծի բոլոր `.ts` ֆայլերը, որոնք սահմանված են `tsconfig.json` ֆայլում (`--build`-ը կարող է բաց թողնել՝ նախագիծը ընթացիկ աշխատանքային գրացուցակում կառուցելու համար):

`tsc {{[-b|--build]}} {{path/to/tsconfig.json}}`

- Գործարկեք կոմպիլյատորը՝ օգտագործելով հրամանի տողի ընտրանքները և տեքստային ֆայլից բերված փաստարկները.:

`tsc @{{args.txt}}`

- Մուտքագրեք JavaScript բազմաթիվ ֆայլեր և թողարկեք միայն սխալները.:

`tsc --allowJs --checkJs --noEmit {{src/**/*.js}}`

- Գործարկեք կոմպիլյատորը ժամացույցի ռեժիմում, որն ինքնաբերաբար վերակազմավորում է կոդը, երբ այն փոխվում է.:

`tsc {{[-w|--watch]}}`
