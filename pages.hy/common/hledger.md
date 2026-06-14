# հլեդջեր

> Հզոր, բարեկամական պարզ տեքստային հաշվապահական ծրագիր:.
> Տես նաև՝ `hledger-ui`, `hledger-web`:.
> Լրացուցիչ տեղեկություններ. <https://hledger.org/hledger.html>:.

- Գրանցեք նոր գործարքները ինտերակտիվ կերպով՝ պահպանելով լռելյայն ամսագրի ֆայլում.:

`hledger add`

- Ներմուծեք նոր գործարքներ `bank.csv`-ից՝ օգտագործելով `bank.csv.rules`՝ փոխարկելու համար՝:

`hledger import {{path/to/bank.csv}}`

- Տպեք բոլոր գործարքները՝ կարդալով մի քանի նշված ամսագրի ֆայլերից.:

`hledger print {{[-f|--file]}} {{path/to/prices-2024.journal}} {{[-f|--file]}} {{path/to/prices-2023.journal}}`

- Ցուցադրել բոլոր հաշիվները, որպես հիերարխիա, և դրանց տեսակները.:

`hledger accounts {{[-t|--tree]}} --types`

- Ցույց տալ ակտիվների և պարտավորությունների հաշվի մնացորդները, ներառյալ զրոները, հիերարխիկորեն.:

`hledger {{[bs|balancesheet]}} {{[-E|--empty]}} {{[-t|--tree]}} --no-elide`

- Ցուցադրել ամսական եկամուտները/ծախսերը/ընդհանուրները, առաջինը՝ ամենամեծը, ամփոփված 2 մակարդակի վրա.:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}} {{[-T|--row-total]}} {{[-A|--average]}} --sort {{[-2|--depth 2]}}`

- Ցույց տալ `assets:bank:checking` հաշվի գործարքները և ընթացիկ մնացորդը՝:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Ցույց տալ սննդի վրա ծախսված գումարը `assets:cash` հաշվից.:

`hledger print assets:cash | hledger {{[-f|--file]}} - {{[-I|--ignore-assertions]}} aregister expenses:food`
