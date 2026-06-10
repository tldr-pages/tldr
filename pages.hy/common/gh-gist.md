#հի էություն

> Աշխատեք GitHub Gists-ի հետ:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_gist>:.

- Ստեղծեք նոր Gist մեկ կամ մի քանի ֆայլերից.:

`gh gist {{[new|create]}} {{path/to/file1 path/to/file2 ...}}`

- Ստեղծեք նոր Gist հատուկ [նկարագրություն] մակագրությամբ.:

`gh gist {{[new|create]}} {{path/to/file1 path/to/file2 ...}} {{[-d|--desc]}} "{{description}}"`

- Խմբագրել էությունը.:

`gh gist edit {{id|url}}`

- Ցուցակե՛ք մինչև 42 բովանդակություն, որոնք պատկանում են ներկայումս մուտք գործած օգտատիրոջը.:

`gh gist {{[ls|list]}} {{[-L|--limit]}} 42`

- Դիտեք Gist-ը լռելյայն դիտարկիչում՝ առանց Markdown-ի ցուցադրման.:

`gh gist view {{id|url}} {{[-w|--web]}} {{[-r|--raw]}}`
