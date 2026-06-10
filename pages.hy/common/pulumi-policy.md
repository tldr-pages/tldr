# pulumi քաղաքականություն

> Կառավարեք ռեսուրսների քաղաքականությունը Pulumi Cloud-ում (Business Critical) կամ տեղական (առանց կազմակերպության ենթահրամանների):.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_policy/>:.

- Ստեղծեք նոր Pulumi քաղաքականության փաթեթ կաղապարից կամ URL-ից.:

`pulumi policy new --dir {{path/to/directory}} {{template|url}}`

- Վավերացնել քաղաքականության շարահյուսությունը: Նախագծի նկատմամբ քաղաքականությունը ստուգելու համար օգտագործեք `pulumi preview`՝:

`pulumi policy validate-config {{organization_name}}/{{policy_pack_name}} {{version}}`

- Նշեք կազմակերպության բոլոր քաղաքականությունները.:

`pulumi policy ls {{[-j|--json]}} {{organization_name}}`

- Հրապարակեք քաղաքականություն Pulumi Cloud-ում.:

`pulumi policy publish {{organization_name}}`

- Միացնել քաղաքականությունը կոնկրետ տարբերակով.:

`pulumi policy enable {{organization_name}}/{{policy_pack_name}} {{latest|version}}`

- Անջատեք քաղաքականությունը որոշակի տարբերակով (կանխադրված բոլոր տարբերակների համար).:

`pulumi policy disable {{organization_name}}/{{policy_pack_name}} --version {{version}}`

- Ցուցադրել օգնությունը.:

`pulumi policy {{[-h|--help]}}`
