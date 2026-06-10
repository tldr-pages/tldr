# pip անիվ

> Ստեղծեք անիվների արխիվներ փաթեթների և կախվածությունների համար:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_wheel/>:.

- Կառուցեք անիվ փաթեթի համար.:

`pip wheel {{package}}`

- Կառուցեք անիվներ փաթեթների համար պահանջների ֆայլում.:

`pip wheel {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Ստեղծեք անիվը որոշակի գրացուցակում.:

`pip wheel {{package}} {{[-w|--wheel-dir]}} {{path/to/directory}}`

- Կառուցեք անիվ առանց կախվածության.:

`pip wheel {{package}} --no-deps`

- Անիվ կառուցել տեղական նախագծից.:

`pip wheel {{path/to/project}}`

- Ստեղծեք անիվ Git պահոցից.:

`pip wheel git+{{https://github.com/user/repo.git}}`
