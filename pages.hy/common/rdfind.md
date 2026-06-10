#րդգտեք

> Գտեք կրկնօրինակ բովանդակությամբ ֆայլեր և ազատվեք դրանցից:.
> Լրացուցիչ տեղեկություններ. <https://rdfind.pauldreik.se/rdfind.1.html>:.

- Բացահայտեք բոլոր կրկնօրինակները տվյալ գրացուցակում և թողարկեք ամփոփագիր.:

`rdfind -dryrun true {{path/to/directory}}`

- Փոխարինեք բոլոր կրկնօրինակները կոշտ հղումներով.:

`rdfind -makehardlinks true {{path/to/directory}}`

- Փոխարինեք բոլոր կրկնօրինակները սիմհղումներով/փափուկ հղումներով.:

`rdfind -makesymlinks true {{path/to/directory}}`

- Ջնջեք բոլոր կրկնօրինակները և մի անտեսեք դատարկ ֆայլերը.:

`rdfind -deleteduplicates true -ignoreempty false {{path/to/directory}}`
