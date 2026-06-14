# typst

> Կազմել Typst ֆայլը PDF-ում:.
> Նշում. ելքի գտնվելու վայրը նշելը պարտադիր չէ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/typst>:.

- Նախաձեռնեք նոր Typst նախագիծը տվյալ գրացուցակում՝ օգտագործելով ձևանմուշ (օրինակ՝ `@preview/charged-ieee`):

`typst init "{{template}}" {{path/to/directory}}`

- Կազմել Typst ֆայլ.:

`typst compile {{path/to/source.typ}} {{path/to/output.pdf}}`

- Դիտեք Typst ֆայլը և վերակազմավորեք փոփոխությունները.:

`typst watch {{path/to/source.typ}} {{path/to/output.pdf}}`

- Թվարկեք համակարգում և տվյալ գրացուցակում հայտնաբերվող բոլոր տառատեսակները.:

`typst --font-path {{path/to/fonts_directory}} fonts`
