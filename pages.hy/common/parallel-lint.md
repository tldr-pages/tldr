# զուգահեռ-lint

> Զուգահեռաբար ստուգեք PHP ֆայլերի շարահյուսությունը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/JakubOnderka/PHP-Parallel-Lint>:.

- Տեղադրեք հատուկ գրացուցակ.:

`parallel-lint {{path/to/directory}}`

- Տեղադրեք գրացուցակը, օգտագործելով նշված թվով զուգահեռ գործընթացներ.:

`parallel-lint -j {{processes}} {{path/to/directory}}`

- Տեղադրեք գրացուցակը, բացառելով նշված գրացուցակը.:

`parallel-lint --exclude {{path/to/excluded_directory}} {{path/to/directory}}`

- Տեղադրեք ֆայլերի գրացուցակը, օգտագործելով ընդլայնման(ների) ստորակետերով բաժանված ցուցակը.:

`parallel-lint -e {{php,html,phpt}} {{path/to/directory}}`

- Տեղադրեք գրացուցակը և արդյունքները թողարկեք որպես JSON:

`parallel-lint --json {{path/to/directory}}`

- Տեղադրեք գրացուցակը և ցույց տվեք Git Blame-ի արդյունքները սխալներ պարունակող տողերի համար.:

`parallel-lint --blame {{path/to/directory}}`
