#պաշարում

> HTTP բեռնման և չափման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://www.joedog.org/siege-manual/>:.

- Փորձարկեք URL-ը լռելյայն կարգավորումներով.:

`siege {{https://example.com}}`

- Փորձարկեք URL-ների ցանկը.:

`siege {{[-f|--file]}} {{path/to/url_list.txt}}`

- Պատահական հերթականությամբ URL-ների թեստային ցուցակը (սիմվոլացնում է ինտերնետ տրաֆիկը).:

`siege {{[-i|--internet]}} {{[-f|--file]}} {{path/to/url_list.txt}}`

- Նշեք URL-ների ցանկը (առանց հարցումների միջև սպասելու).:

`siege {{[-b|--benchmark]}} {{[-f|--file]}} {{path/to/url_list.txt}}`

- Սահմանեք միաժամանակյա կապերի քանակը.:

`siege {{[-c|--concurrent]}} {{50}} {{[-f|--file]}} {{path/to/url_list.txt}}`

- Սահմանեք, թե որքան ժամանակ կշարունակվի պաշարումը.:

`siege {{[-t|--time]}} {{30s}} {{[-f|--file]}} {{path/to/url_list.txt}}`
