#բրետանի

> Գեղեցիկ տպագիր Haskell աղբյուրի ֆայլեր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/lspitzner/brittany#readme>:.

- Ձևաչափեք Haskell սկզբնաղբյուր ֆայլը և տպեք արդյունքը `stdout`:

`brittany {{path/to/file.hs}}`

- Ձևաչափեք բոլոր Haskell սկզբնաղբյուր ֆայլերը ընթացիկ գրացուցակում տեղում.:

`brittany --write-mode=inplace {{*.hs}}`

- Ստուգեք, արդյոք Haskell աղբյուրի ֆայլը փոփոխությունների կարիք ունի և արդյունքը նշեք ծրագրի ելքի կոդի միջոցով.:

`brittany --check-mode {{path/to/file.hs}}`

- Ձևաչափեք Haskell սկզբնաղբյուր ֆայլը, օգտագործելով նշված քանակությամբ բացատներ յուրաքանչյուր ներքևման մակարդակի և տողի երկարության համար.:

`brittany --indent {{4}} --columns {{100}} {{path/to/file.hs}}`

- Ձևաչափեք Haskell աղբյուրի ֆայլը ըստ նշված կազմաձևման ֆայլում սահմանված ոճի.:

`brittany --config-file {{path/to/config.yaml}} {{path/to/file.hs}}`
