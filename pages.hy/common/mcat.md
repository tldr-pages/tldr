#mcat

> Վերլուծեք, փոխարկեք և նախադիտեք ֆայլերը (ներառյալ Markdown), գրացուցակները, պատկերները և տեսանյութերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Skardyy/mcat#example-usage>:.

- Ցուցադրել ֆայլի բովանդակությունը.:

`mcat {{path/to/file}}`

- Ցուցադրել Markdown ֆայլը հատուկ թեմայով.:

`mcat {{[-t|--theme]}} {{theme_name}} {{path/to/file.md}}`

- Ցուցադրել պատկեր կամ տեսանյութ ներդիրում.:

`mcat {{[-i|--output inline]}} {{path/to/file}}`

- Փոխակերպեք ֆայլը որոշակի ձևաչափի (օրինակ՝ `html`, `md`, `image`):

`mcat {{[-o|--output]}} {{format}} {{path/to/file}}`

- Թվարկեք գրացուցակի բովանդակությունը.:

`mcat {{path/to/directory}}`

- Թվարկեք գրացուցակի բովանդակությունը, ներառյալ թաքնված ֆայլերը.:

`mcat {{[-a|--hidden]}} {{path/to/directory}}`

- Ցուցադրել բովանդակությունը առանց էջավորման.:

`mcat {{[-P|--paging never]}} {{path/to/file}}`
