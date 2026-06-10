# noseyparker

> Սկանավորեք տեքստը և Git պատմությունը գաղտնիքների և զգայուն տեղեկատվության համար:.
> Նշում. յուրաքանչյուր սկանավորման համար օգտագործեք տվյալների պահեստի առանձին գրացուցակ (`--datastore`):.
> Տես նաև՝ `trufflehog`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/praetorian-inc/noseyparker#usage-examples>:.

- Սկանավորեք տեղական ֆայլը կամ գրացուցակը գաղտնիքների համար.:

`noseyparker scan {{path/to/file_or_directory}} {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Ցույց տալ հաշվետվություն նախորդ սկանավորումից.:

`noseyparker report {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Ցույց տալ հաշվետվություն տարբեր ձևաչափով (կանխադրվածը `human` է):

`noseyparker report {{[-d|--datastore]}} {{path/to/datastore.np}} {{[-f|--format]}} {{human|json|jsonl|sarif}}`

- Գաղտնիքների համար սկանավորեք հեռակա Git ռեպո (և Git պատմությունը).:

`noseyparker scan --git-url {{url}} {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Սկանավորեք օգտատիրոջ կամ կազմակերպության բոլոր GitHub պահոցները գաղտնիքների համար.:

`noseyparker scan {{--github-user|--github-organization}} {{username_or_org_name}} {{[-d|--datastore]}} {{path/to/datastore.np}}`

- Թվարկեք սկանավորման բոլոր կանոնները.:

`noseyparker rules list`

- Թվարկեք օգտվողի կամ կազմակերպության բոլոր GitHub պահեստները.:

`noseyparker github repos list {{--user|--organization}} {{username_or_org_name}}`
