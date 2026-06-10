# pulumi stack

> Կառավարեք կույտերը և դիտեք կույտերի վիճակը:.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>:.

- Ստեղծեք նոր կույտ.:

`pulumi stack init {{stack_name}}`

- Ցուցադրել կույտի վիճակը ռեսուրսների URN-ների հետ միասին.:

`pulumi stack {{[-u|--show-urns]}}`

- Ցուցակեք կույտերը ընթացիկ նախագծում.:

`pulumi stack ls`

- Ցուցակեք կույտերը բոլոր նախագծերում.:

`pulumi stack ls {{[-a|--all]}}`

- Ընտրեք ակտիվ բուրգ.:

`pulumi stack select {{stack_name}}`

- Ջնջել կույտը.:

`pulumi stack rm {{stack_name}}`

- Ցուցադրել փաթեթի արդյունքները, ներառյալ գաղտնիքները, պարզ տեքստով.:

`pulumi stack output --show-secrets`

- Արտահանել կույտի վիճակը JSON ֆայլ.:

`pulumi stack export --file {{path/to/file.json}}`
