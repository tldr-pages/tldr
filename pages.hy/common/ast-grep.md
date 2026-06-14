# ast-grep

> Փնտրեք, ծածկեք և վերագրեք կոդը՝ օգտագործելով AST նախշերը:.
> Լրացուցիչ տեղեկություններ. <https://ast-grep.github.io/reference/cli.html>:.

- Որոնեք օրինակ ֆայլերում.:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{path/to/file}}`

- Որոնեք օրինաչափություն որոշակի լեզվով.:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-l|--lang]}} {{python}} {{path/to/directory}}`

- Վերագրեք օրինաչափությանը համապատասխանող կոդը.:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-r|--rewrite]}} '{{replacement}}' {{path/to/file}}`

- Գործարկեք կանոնները կազմաձևման ֆայլից.:

`ast-grep scan {{[-r|--rule]}} {{path/to/rule.yml}} {{path/to/directory}}`

- Ինտերակտիվ որոնեք և վերագրեք կոդը.:

`ast-grep run {{[-p|--pattern]}} '{{pattern}}' {{[-i|--interactive]}} {{path/to/directory}}`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`ast-grep {{run}} {{[-h|--help]}}`
