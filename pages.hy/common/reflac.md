# reflac

> Նորից սեղմեք FLAC ֆայլերը տեղում՝ պահպանելով մետատվյալները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/chungy/reflac#running>:.

- Վերաճնշել FLAC ֆայլերի գրացուցակը.:

`reflac {{path/to/directory}}`

- Միացնել առավելագույն սեղմումը (շատ դանդաղ).:

`reflac {{[-8|--best]}} {{path/to/directory}}`

- Ցուցադրել ֆայլերի անունները, երբ դրանք մշակվում են.:

`reflac {{[-v|--verbose]}} {{path/to/directory}}`

- Կրկնվել ենթագրքերում՝:

`reflac {{[-r|--recursive]}} {{path/to/directory}}`

- Պահպանել ֆայլի փոփոխման ժամանակները.:

`reflac --preserve {{path/to/directory}}`
