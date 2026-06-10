#լյուկ

> Ժամանակակից, ընդարձակելի Python ծրագրի ղեկավար:.
> Տես նաև՝ `poetry`:.
> Լրացուցիչ տեղեկություններ. <https://hatch.pypa.io/latest/cli/reference/>:.

- Ստեղծեք նոր Hatch նախագիծ.:

`hatch new {{project_name}}`

- Նախաձեռնել Hatch-ը գոյություն ունեցող նախագծի համար.:

`hatch new --init`

- Կառուցեք Hatch նախագիծ.:

`hatch build`

- Հեռացրեք շինարարական արտեֆակտները.:

`hatch clean`

- Ստեղծեք կանխադրված միջավայր `pyproject.toml` ֆայլում սահմանված կախվածություններով.:

`hatch env create`

- Ցուցադրել շրջակա միջավայրի կախվածությունը որպես աղյուսակ.:

`hatch dep show table`
