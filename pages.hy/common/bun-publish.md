# bun հրապարակել

> Հրապարակեք փաթեթ npm ռեեստրում:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/publish>:.

- Հրապարակեք ընթացիկ փաթեթը npm ռեգիստրում.:

`bun publish`

- Հրապարակեք փաթեթ որոշակի գրացուցակից.:

`bun publish {{path/to/package_directory}}`

- Հրապարակեք շրջանակային փաթեթ՝ հատուկ մուտքի մակարդակով.:

`bun publish --access {{public|restricted}}`

- Փաթեթ հրապարակեք մաքսային գրանցամատյանում.:

`bun publish --registry {{registry}}`

- Անցեք չոր վազք՝ տեսնելու, թե ինչ կհրապարակվի առանց վերբեռնելու.:

`bun publish --dry-run`

- Հրապարակեք փաթեթ հատուկ բաշխման պիտակով.:

`bun publish --tag {{tag_name}}`

- Հրապարակեք մեկանգամյա գաղտնաբառով 2FA-ով միացված հաշիվների համար.:

`bun publish --otp {{one_time_password}}`

- Հրապարակել՝ օգտագործելով նույնականացման հատուկ տեսակ.:

`bun publish --auth-type {{web|legacy}}`
