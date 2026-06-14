# բեռնախցիկ

> Կոդերի վրա գործարկեք լինտերներ, ձևաչափիչներ և անվտանգության անալիզատորներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.trunk.io/code-quality/overview/getting-started/commands-reference>:.

- Նախաձեռնել բեռնախցիկը պահեստում.:

`trunk init`

- Գործարկեք բոլոր կիրառելի լինտերներն ու ձևաչափերը փոխված ֆայլերի վրա.:

`trunk check`

- Գործարկել linters և ֆորմատիչներ հատուկ ֆայլերի վրա.:

`trunk check {{path/to/file1 path/to/file2 ...}}`

- Ձևաչափեք ֆայլերը տեղում.:

`trunk fmt`

- Թվարկեք բոլոր հասանելի գործիքները և դրանց կարգավիճակը.:

`trunk tools list`

- Միացնել գործիքը որոշակի տարբերակով.:

`trunk tools enable {{tool}}@{{version}}`

- Տպել գործողության կատարման պատմությունը.:

`trunk actions history {{action}}`
