#թանաքարտ

> GNU Makefile-ի ոճով SVG-ն արտահանվում է Inkscape-ի հետնամասի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wader/inkmake#usage>:.

- Արտահանեք SVG ֆայլ, որն իրականացնում է նշված Inkfile-ը.:

`inkmake {{path/to/Inkfile}}`

- Կատարեք Inkfile և ցուցադրեք մանրամասն տեղեկատվություն.:

`inkmake {{[-v|--verbose]}} {{path/to/Inkfile}}`

- Կատարեք Inkfile՝ նշելով SVG մուտքային ֆայլ(ներ) և ելքային ֆայլ.:

`inkmake {{[-s|--svg]}} {{path/to/file.svg}} {{[-o|--out]}} {{path/to/output_image}} {{path/to/Inkfile}}`

- Օգտագործեք հատուկ Inkscape երկուական որպես հետին պլան.:

`inkmake {{[-i|--inkscape]}} {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}`

- Ցուցադրել օգնությունը.:

`inkmake {{[-h|--help]}}`
