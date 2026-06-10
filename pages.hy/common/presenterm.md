#հաղորդավար

> Տերմինալի վրա հիմնված սլայդերի ցուցադրման գործիք, որը ներկայացնում է նիշերի ներկայացումներ:.
> Լրացուցիչ տեղեկություններ. <https://mfontanini.github.io/presenterm/>:.

- Ցուցադրել ներկայացում.:

`presenterm {{path/to/slides.md}}`

- Ցուցադրել ներկայացում հատուկ թեմայով.:

`presenterm --theme {{dark|light|tokyonight-storm|...}} {{path/to/slides.md}}`

- Թվարկեք բոլոր առկա թեմաները.:

`presenterm --list-themes`

- Արտահանել ներկայացումը PDF.:

`presenterm --export-pdf --output {{path/to/output.pdf}} {{path/to/slides.md}}`

- Ցուցադրել ներկայացում կոդի հատվածի կատարումը միացված.:

`presenterm --enable-snippet-execution {{path/to/slides.md}}`

- Ստուգեք, որ ներկայացման բովանդակությունը տեղավորվում է տերմինալում.:

`presenterm --validate-overflows {{path/to/slides.md}}`
