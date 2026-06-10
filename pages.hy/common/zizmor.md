# zizmor

> Գտեք անվտանգության խնդիրները GitHub Actions-ի աշխատանքային հոսքերում և գործողությունների սահմանումներում:.
> Լրացուցիչ տեղեկություններ. <https://docs.zizmor.sh/quickstart/>:.

- Վերստուգեք ընթացիկ գրացուցակի բոլոր աշխատանքային հոսքերն ու գործողությունները.:

`zizmor .`

- Աուդիտ որոշակի աշխատանքային հոսքի ֆայլ.:

`zizmor {{path/to/workflow.yml}}`

- Աուդիտ անցկացրեք GitHub-ի հեռավոր պահոցում (պահանջվում է GitHub նշան).:

`zizmor --gh-token {{token}} {{username/repository}}`

- Գործարկեք միայն անցանց աուդիտ (ցանցային հարցումներ չկան).:

`zizmor {{[-o|--offline]}} {{path/to/workflow.yml}}`

- Արդյունքները SARIF ձևաչափով.:

`zizmor --format sarif {{path/to/workflow.yml}}`

- Զտել գտածոները ըստ նվազագույն խստության.:

`zizmor --min-severity {{informational|low|medium|high}} .`

- Ցուցադրել օգնությունը.:

`zizmor {{[-h|--help]}}`

- Ցուցադրման տարբերակը:

`zizmor {{[-v|--version]}}`
