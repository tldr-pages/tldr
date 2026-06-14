# tldr-lint

> Լինտ և ձևաչափեք `tldr` էջերը:.
> Նշում. `tldrl`-ը կարող է օգտագործվել որպես `tldr-lint`-ի կեղծանուն:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tldr-pages/tldr-lint#usage>:.

- Տեղադրեք մեկ էջ կամ գրացուցակի բոլոր էջերը.:

`tldr-lint {{path/to/page_or_directory}}`

- Անտեսեք հատուկ `tldr-lint` սխալի կոդերը, երբ ցցվում է.:

`tldr-lint {{[-I|--ignore]}} {{TLDR001,TLDR002,...}}`

- Ձևաչափեք կոնկրետ էջը `stdout`-ի.:

`tldr-lint {{[-f|--format]}} {{path/to/page.md}}`

- Ձևաչափեք էջը տեղում.:

`tldr-lint {{[-f|--format]}} {{[-i|--in-place]}} {{path/to/page.md}}`
