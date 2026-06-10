#շարժիչ

> Կարգավորեք PropelAuth նույնականացումը հնարավորինս արագ և հեշտությամբ:.
> Լրացուցիչ տեղեկություններ. <https://docs.propelauth.com/reference/api/cli>:.

- Մուտք գործեք PropelAuth՝ օգտագործելով <https://auth.propelauth.com/api_keys/personal>-ից ստեղծված API բանալի:

`propelauth login`

- Սահմանեք լռելյայն PropelAuth նախագիծը CLI-ի համար: Եթե լռելյայն նախագիծ սահմանված չէ, համակարգը կպահանջի ընտրել Նախագիծ ամեն անգամ, երբ գործարկվեն որոշակի հրամաններ.:

`propelauth set-default-project`

- Տեղադրեք PropelAuth վավերացումը հավելվածում: Եթե գրացուցակ չկա, ապա օգտագործվում է ընթացիկ գրացուցակը.:

`propelauth setup {{[-f|--framework]}} {{path/to/directory}}`

- Դուրս գրեք CLI-ն PropelAuth-ից.:

`propelauth logout`
