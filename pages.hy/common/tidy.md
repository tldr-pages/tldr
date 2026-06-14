#կոկիկ

> Մաքրել և գեղեցիկ տպել HTML, XHTML և XML ֆայլերը:.
> Նշում. `tidy`-ը չի կարող պահպանել բնօրինակը:.
> Լրացուցիչ տեղեկություններ. <https://api.html-tidy.org/tidy/tidylib_api_next/group__options__cli.html#gad7a9fcaf7b2a712a82e625e84c042b28>:.

- Գեղեցիկ տպեք HTML ֆայլ.:

`tidy {{path/to/file.html}}`

- Միացնել նահանջը, տողերը փաթաթելով 100-ով, պահպանելով `output.html`:

`tidy {{[-i|--indent]}} y {{[-w|--wrap]}} 100 {{[-o|-output]}} {{path/to/output.html}} {{path/to/file.html}}`

- Փոխեք HTML ֆայլը տեղում՝ օգտագործելով կազմաձևման ֆայլը.:

`tidy -config {{path/to/configuration}} {{[-m|-modify]}} {{path/to/file.html}}`
