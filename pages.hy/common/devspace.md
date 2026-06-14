# devspace

> Մշակել, տեղակայել և վրիպազերծել հավելվածներ Kubernetes-ի ներսում:.
> Լրացուցիչ տեղեկություններ. <https://www.devspace.sh/docs/cli>:.

- Նախաձեռնեք նոր DevSpace նախագիծը ընթացիկ գրացուցակում.:

`devspace init`

- Սկսեք զարգացման ռեժիմը նավահանգիստների վերահասցեավորման, ֆայլերի համաժամացման և տերմինալի մուտքի միջոցով.:

`devspace dev`

- Սկսեք զարգացման ռեժիմը որոշակի անվանատարածքում.:

`devspace dev {{[-n|--namespace]}} {{namespace}}`

- Տեղադրեք նախագիծը Kubernetes-ում.:

`devspace deploy`

- Տեղադրեք նախագիծը հատուկ պրոֆիլով.:

`devspace deploy {{[-p|--profile]}} {{profile-name}}`

- Կառուցեք բոլոր սահմանված պատկերները.:

`devspace build`

- Հետևեք տեղեկամատյաններին պատիճից.:

`devspace logs {{[-f|--follow]}}`

- Բացեք DevSpace UI-ը զննարկիչում.:

`devspace ui`
