# pip ներբեռնում

> Ներբեռնեք Python փաթեթները՝ առանց դրանք տեղադրելու:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_download/>:.

- Ներբեռնեք փաթեթի անիվը կամ աղբյուրի արխիվը ընթացիկ գրացուցակում.:

`pip download {{package}}`

- Ներբեռնեք փաթեթի որոշակի տարբերակ.:

`pip download {{package}}=={{version}}`

- Ներբեռնեք փաթեթը և դրա կախվածությունները որոշակի գրացուցակում.:

`pip download {{package}} {{[-d|--dest]}} {{path/to/directory}}`

- Ներբեռնեք փաթեթ հատուկ հարթակի և Python տարբերակի համար.:

`pip download {{package}} --only-binary :all: --platform {{platform}} --python-version {{version}}`

- Ներբեռնեք փաթեթ կոնկրետ ինդեքսի URL-ից.:

`pip download {{package}} {{[-i|--index-url]}} {{url}}`
