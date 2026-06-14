# gopass

> Ստանդարտ Unix գաղտնաբառերի կառավարիչ թիմերի համար: Գրված է Go-ում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/gopasspw/gopass/tree/master/docs/commands>:.

- Նախաձեռնեք կազմաձևման կարգավորումները.:

`gopass init`

- Ստեղծեք նոր գրառում.:

`gopass new`

- Ցույց տալ բոլոր խանութները.:

`gopass mounts`

- Տեղադրեք ընդհանուր Git խանութ.:

`gopass mounts add {{store_name}} {{git_repo_url}}`

- Որոնեք ինտերակտիվ կերպով, օգտագործելով հիմնաբառ.:

`gopass show {{keyword}}`

- Որոնել հիմնաբառի միջոցով.:

`gopass find {{keyword}}`

- Համաժամացրեք բոլոր տեղադրված խանութները.:

`gopass sync`

- Ցույց տալ որոշակի գաղտնաբառի մուտքագրում.:

`gopass {{store_name|path/to/directory|email@email.com}}`
