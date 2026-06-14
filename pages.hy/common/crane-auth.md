# կռունկ հեղինակություն

> Մուտք գործեք կամ մուտք գործեք հավատարմագրեր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_auth.md>:.

- Կատարեք `crane auth` ենթահրամանը՝:

`crane auth {{subcommand}}`

- Իրականացնել հավատարմագրային օգնական.:

`crane auth get {{registry_address}} {{[-h|--help]}}`

- Մուտք գործեք գրանցամատյան.:

`crane auth login {{registry_address}} {{[-h|--help]}} {{[-p|--password]}} {{password}} {{-password-stdin}} {{[-u|--username]}} {{username}}`

- Դուրս գալ ռեեստրից.:

`crane auth logout {{registry_address}} {{[-h|--help]}}`

- Ստացեք նշան հեռավոր պահեստի համար.:

`crane auth token {{registry_address}} {{[-H|--header]}} {{[-h|--help]}} {{[-m|--mount]}} {{scope1 scope2 ...}} --push`

- Ցուցադրել օգնությունը.:

`crane auth {{[-h|--help]}}`
