# կռունկների ռեեստր

> Այս հրամանը ծառայում է ռեեստրի ներդրմանը ավտոմատ ընտրված միացքում (`:0`), `$PORT` կամ `--address`:.
> Հրամանն արգելափակվում է, մինչ սերվերն ընդունում է հրումներ և ձգումներ, և բովանդակությունը կարող է պահվել հիշողության մեջ և սկավառակի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>:.

- Ծառայել ռեեստրի ներդրում.:

`crane registry serve`

- Հասցեն լսելու համար.:

`crane registry serve --address {{address_name}}`

- Ուղ դեպի գրացուցակ, որտեղ բլբերը կպահվեն.:

`crane registry serve --disk {{path/to/store_directory}}`

- Ցուցադրել օգնություն `crane registry`-ի համար՝:

`crane registry {{[-h|--help]}}`

- Ցուցադրել օգնություն `crane registry serve`-ի համար՝:

`crane registry serve {{[-h|--help]}}`
