# զրոյական ճանկ

> Արագ, փոքր և լիովին ինքնավար AI օգնական ենթակառուցվածք:.
> Որոշ ենթահրամաններ, ինչպիսիք են `onboard`, `models`, `service` և այլն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Տես նաև՝ `openclaw`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/zeroclaw-labs/zeroclaw#quick-start>:.

- Նախաձեռնել աշխատանքային տարածքը և կազմաձևումը (արագ կարգավորում).:

`zeroclaw onboard --api-key {{api_key}} --provider {{openrouter|anthropic|openai|...}}`

- Գործարկեք ամբողջական ինտերակտիվ ներբեռնման հրաշագործը.:

`zeroclaw onboard --interactive`

- Ուղարկեք մեկ հաղորդագրություն AI գործակալին.:

`zeroclaw agent {{[-m|--message]}} "{{Hello, ZeroClaw!}}"`

- Սկսեք ինտերակտիվ զրույցի ռեժիմը.:

`zeroclaw agent`

- Գործարկեք gateway սերվերը (կանխադրված՝ 127.0.0.1:8080):

`zeroclaw gateway`

- Սկսեք լիարժեք ինքնավար գործարկման ժամանակը (դարպաս + ալիք + սրտի զարկ).:

`zeroclaw daemon`

- Ստուգեք համակարգի կարգավիճակը.:

`zeroclaw status`

- Գործարկել ախտորոշում.:

`zeroclaw doctor`
