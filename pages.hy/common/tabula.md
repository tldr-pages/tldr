# աղյուսակ

> Քաղեք աղյուսակները PDF ֆայլերից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tabulapdf/tabula-java#commandline-usage-examples>:.

- Բոլոր աղյուսակները հանեք PDF-ից CSV ֆայլ.:

`tabula {{[-o|--outfile]}} {{file.csv}} {{file.pdf}}`

- Բոլոր աղյուսակները հանեք PDF-ից JSON ֆայլ.:

`tabula {{[-f|--format]}} JSON {{[-o|--outfile]}} {{file.json}} {{file.pdf}}`

- Քաղեք աղյուսակները PDF-ի 1-ին, 2-րդ, 3-րդ և 6-րդ էջերից.:

`tabula {{[-p|--pages]}} 1-3,6 {{file.pdf}}`

- Քաղեք աղյուսակներ PDF-ի 1-ին էջից՝ գուշակելով, թե էջի որ հատվածը պետք է ուսումնասիրվի.:

`tabula {{[-g|--guess]}} {{[-p|--pages]}} 1 {{file.pdf}}`

- Քաղեք բոլոր աղյուսակները PDF-ից՝ օգտագործելով իշխող տողերը՝ բջիջների սահմանները որոշելու համար.:

`tabula {{[-r|--spreadsheet]}} {{file.pdf}}`

- Քաղեք բոլոր աղյուսակները PDF-ից՝ օգտագործելով դատարկ տարածք՝ բջիջների սահմանները որոշելու համար.:

`tabula {{[-n|--no-spreadsheet]}} {{file.pdf}}`
