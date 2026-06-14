# ծառերդ

> Դիտեք նշագրման ֆայլերը ծառերի վրա հիմնված նավիգացիայով և ինտերակտիվ TUI-ով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Epistates/treemd#usage>:.

- Բացեք նշագրման ֆայլ ինտերակտիվ TUI ռեժիմում.:

`treemd {{path/to/file.md}}`

- Նշեք բոլոր վերնագրերը նշագրման ֆայլում.:

`treemd {{[-l|--list]}} {{path/to/file.md}}`

- Ցույց տվեք նշագրման ֆայլի վերնագրի ծառի կառուցվածքը.:

`treemd --tree {{path/to/file.md}}`

- Արտահանեք որոշակի բաժին ըստ վերնագրի անունով.:

`treemd {{[-s|--section]}} {{heading_name}} {{path/to/file.md}}`

- Զտել վերնագրերը հատուկ օրինակով.:

`treemd {{[-l|--list]}} --filter {{pattern}} {{path/to/file.md}}`

- Հարցում և հանում նշագրման կառուցվածքը՝ օգտագործելով treemd հարցման լեզուն.:

`treemd {{[-q|--query]}} '{{.h2 | text}}' {{path/to/file.md}}`
