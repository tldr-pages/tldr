# պոեզիա նոր

> Ստեղծեք նոր Poetry նախագիծ կոնկրետ գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#new>:.

- Ստեղծեք նոր նախագիծ (կանխադրված է `src` դասավորությունը):

`poetry new {{path/to/directory}}`

- Ստեղծեք նոր նախագիծ՝ ինտերակտիվ կերպով խնդրելով կազմաձևման մանրամասները.:

`poetry new {{path/to/directory}} {{[-i|--interactive]}}`

- Ստեղծեք նոր նախագիծ հատուկ փաթեթի անունով.:

`poetry new {{path/to/directory}} --name {{package_name}}`

- Ստեղծեք նոր նախագիծ՝ օգտագործելով հարթ դասավորությունը (առանց `src` գրացուցակի).:

`poetry new {{path/to/directory}} --flat`

- Ստեղծեք նոր նախագիծ կոնկրետ հեղինակի հետ.:

`poetry new {{path/to/directory}} --author "{{Name <email@example.com>}}"`

- Ստեղծեք նոր նախագիծ հատուկ README ձևաչափով.:

`poetry new {{path/to/directory}} --readme {{md|rst|txt|...}}`
