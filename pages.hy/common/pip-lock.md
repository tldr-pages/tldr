# pip lock

> Կողպեք Python փաթեթները և դրանց կախվածությունները վերարտադրվող ֆայլի մեջ:.
> `pip`-ի փորձարարական հատկանիշ:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_lock/>:.

- Ստեղծեք `pylock.toml` ընթացիկ նախագծի համար.:

`pip lock {{[-e|--editable]}} .`

- Կողպեք կախվածությունը պահանջների ֆայլից.:

`pip lock {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Նշեք հատուկ ելքային ֆայլ կողպեքի համար.:

`pip lock {{[-o|--output]}} {{path/to/lockfile.toml}}`

- Կողպեք որոշակի փաթեթ և դրա կախվածությունները.:

`pip lock {{package}}`
