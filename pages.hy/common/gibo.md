#գիբո

> Ստացեք gitignore կաթսաներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/simonwhitaker/gibo>:.

- Ցուցակեք առկա կաթսաները.:

`gibo list`

- Գրեք կաթսա `stdout` հասցեին՝:

`gibo dump {{boilerplate}}`

- Գրեք կաթսա `.gitignore` հասցեին՝:

`gibo dump {{boilerplate}} >>{{.gitignore}}`

- Որոնեք կաթսայատներ, որոնք պարունակում են տվյալ տող.:

`gibo search {{string}}`

- Թարմացրեք առկա տեղական կաթսաները.:

`gibo update`
