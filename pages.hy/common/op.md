# op

> Պաշտոնական CLI 1Password-ի աշխատասեղանի հավելվածի համար:.
> Լրացուցիչ տեղեկություններ. <https://developer.1password.com/docs/cli/reference/>:.

- Մուտք գործեք 1Password հաշիվ.:

`op signin`

- Նշեք բոլոր պահոցները.:

`op vault list`

- Տպել ապրանքի մանրամասները JSON ձևաչափով.:

`op item get {{item_name}} --format json`

- Ստեղծեք նոր տարր՝ լռելյայն պահոցում կատեգորիայով.:

`op item create --category {{category_name}}`

- Հղված գաղտնիքը տպեք `stdout`-ում՝:

`op read {{secret_reference}}`

- Արտահանված միջավայրի փոփոխականներից գաղտնի հղումներ փոխանցեք հրամանին.:

`op run -- {{command}}`

- Անցեք գաղտնի հղումներ շրջակա միջավայրի ֆայլից հրամանի.:

`op run --env-file {{path/to/env_file.env}} -- {{command}}`

- Կարդացեք գաղտնի հղումները ֆայլից և պահեք պարզ տեքստի գաղտնիքները ֆայլում.:

`op inject --in-file {{path/to/input_file}} --out-file {{path/to/output_file}}`
