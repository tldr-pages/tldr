# csvgrep

> Զտել CSV տողերը տողի և նախշի համապատասխանությամբ:.
> Ներառված է csvkit-ում:.
> Լրացուցիչ տեղեկություններ. <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>:.

- Գտեք տողեր, որոնք ունեն որոշակի տող 1-ին սյունակում.:

`csvgrep {{[-c|--columns]}} {{1}} {{[-m|--match]}} {{string_to_match}} {{data.csv}}`

- Գտեք տողեր, որոնցում 3-րդ կամ 4-րդ սյունակները համապատասխանում են որոշակի `regex`-ին:

`csvgrep {{[-c|--columns]}} {{3,4}} {{[-r|--regex]}} {{regex}} {{data.csv}}`

- Գտեք տողեր, որոնցում «անուն» սյունակը ՉԻ ներառում «John Doe» տողը.:

`csvgrep {{[-i|--invert-match]}} {{[-c|--columns]}} {{name}} {{[-m|--match]}} "{{John Doe}}" {{data.csv}}`
