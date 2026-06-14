# secrethub

> Պահպանեք գաղտնիքները կազմաձևման ֆայլերից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/secrethub/secrethub-cli>:.

- Տպեք գաղտնիք `stdout` հասցեով՝:

`secrethub read {{path/to/secret}}`

- Ստեղծեք պատահական արժեք և պահեք այն որպես նոր կամ թարմացված գաղտնիք.:

`secrethub generate {{path/to/secret}}`

- Պահպանեք արժեքը clipboard-ից որպես նոր կամ թարմացված գաղտնիք.:

`secrethub write --clip {{path/to/secret}}`

- Պահպանեք `stdin`-ում տրված արժեքը որպես նոր կամ թարմացված գաղտնիք.:

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- Վերստուգեք պահեստը կամ գաղտնիքը.:

`secrethub audit {{path/to/repo_or_secret}}`
