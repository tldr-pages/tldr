# տեկտոնիկ

> Ժամանակակից, ինքնուրույն TeX/LaTeX շարժիչ:.
> Լրացուցիչ տեղեկություններ. <https://tectonic-typesetting.github.io/book/latest/>:.

- Կազմեք առանձին TeX/LaTeX ֆայլ.:

`tectonic -X compile {{path/to/file.tex}}`

- Կազմեք ինքնուրույն TeX/LaTeX ֆայլ՝ synctex տվյալների հետ.:

`tectonic -X compile --synctex {{path/to/file.tex}}`

- Նախաձեռնեք տեկտոնական նախագիծ ընթացիկ գրացուցակում.:

`tectonic -X init`

- Նախաձեռնեք տեկտոնական նախագիծ նշված գրացուցակում.:

`tectonic -X new {{project_name}}`

- Կառուցեք նախագիծը ընթացիկ գրացուցակում.:

`tectonic -X build`

- Սկսեք դիտորդ՝ փոփոխության դեպքում նախագիծը ընթացիկ գրացուցակում կառուցելու համար.:

`tectonic -X watch`
