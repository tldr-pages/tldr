#բարակ

> Վերլուծել և օպտիմիզացնել Docker պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/slimtoolkit/slim#usage-details>:.

- Սկսեք Slim-ը ինտերակտիվ ռեժիմում.:

`slim`

- Վերլուծեք Docker շերտերը կոնկրետ պատկերից.:

`slim xray --target {{image:tag}}`

- Տեղադրեք Dockerfile:

`slim lint --target {{path/to/Dockerfile}}`

- Վերլուծեք և ստեղծեք օպտիմիզացված Docker պատկեր.:

`slim build {{image:tag}}`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`slim {{subcommand}} --help`
