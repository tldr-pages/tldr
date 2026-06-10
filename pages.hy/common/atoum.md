#ատում

> Պարզ, ժամանակակից և ինտուիտիվ միավորի փորձարկման շրջանակ PHP-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://atoum.readthedocs.io/en/latest/option_cli.html>:.

- Նախաձեռնեք կազմաձևման ֆայլը.:

`atoum --init`

- Գործարկել բոլոր թեստերը.:

`atoum`

- Գործարկել թեստերը՝ օգտագործելով նշված կազմաձևման ֆայլը.:

`atoum {{[-c|--configuration]}} {{path/to/file}}`

- Գործարկել հատուկ թեստային ֆայլ.:

`atoum {{[-f|--files]}} {{path/to/file}}`

- Գործարկեք թեստերի հատուկ գրացուցակ.:

`atoum {{[-d|--directories]}} {{path/to/directory}}`

- Գործարկեք բոլոր թեստերը որոշակի անվանատարածքի տակ.:

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- Գործարկեք բոլոր թեստերը հատուկ պիտակով.:

`atoum {{[-t|--tags]}} {{tag}}`

- Բեռնել սովորական bootstrap ֆայլը նախքան թեստերը կատարելը.:

`atoum {{[-bf|--bootstrap-file]}} {{path/to/file}}`
