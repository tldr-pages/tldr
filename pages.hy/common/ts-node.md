# ts-հանգույց

> Գործարկեք TypeScript կոդը ուղղակիորեն, առանց որևէ կոմպիլյացիայի:.
> Լրացուցիչ տեղեկություններ. <https://typestrong.org/ts-node/docs/options/>:.

- Կատարեք TypeScript ֆայլ առանց կոմպիլյացիայի (Node + `tsc`):

`ts-node {{path/to/file.ts}}`

- Կատարեք TypeScript ֆայլ առանց `tsconfig.json` բեռնելու:

`ts-node --skipProject {{path/to/file.ts}}`

- Գնահատեք TypeScript ծածկագիրը որպես բառացի.:

`ts-node {{[-e|--eval]}} '{{console.log("Hello World")}}'`

- Գործարկեք TypeScript ֆայլը սցենարի ռեժիմում.:

`ts-node --script-mode {{path/to/file.ts}}`

- Տեղափոխեք TypeScript ֆայլը JavaScript-ում՝ առանց այն գործարկելու.:

`ts-node {{[-T|--transpileOnly]}} {{path/to/file.ts}}`

- Ցուցադրել օգնությունը.:

`ts-node {{[-h|--help]}}`
