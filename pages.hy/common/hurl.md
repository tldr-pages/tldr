# նետում

> Գործարկեք և փորձարկեք HTTP հարցումները, որոնք սահմանված են պարզ տեքստային ձևաչափով:.
> Կառավարվում է `curl`-ով:.
> Լրացուցիչ տեղեկություններ. <https://hurl.dev/docs/manual.html>:.

- Գործարկել HTTP հարցումները ֆայլից.:

`hurl {{path/to/file.hurl}}`

- Գործարկեք HTTP հարցումները և օգտագործեք փոփոխականը.:

`hurl --variable {{variable_name}}={{value}} {{path/to/file.hurl}}`

- Գործարկեք HTTP հարցումները գաղտնիքներով, որոնք պետք է խմբագրվեն տեղեկամատյաններում և հաշվետվություններում.:

`hurl --secret {{secret_name}}={{value}} {{path/to/file.hurl}}`

- Գործարկեք HTTP հարցումները և ներարկեք փոփոխականներ և գաղտնիք ֆայլից.:

`hurl --variables-file {{path/to/variables_file}} --secrets-file {{path/to/secrets_file}} {{path/to/file.hurl}}`

- Գործարկեք հատուկ HTTP հարցումներ ֆայլից՝ 2-ից 5-րդ մուտքից.:

`hurl --from-entry 2 --to-entry 5 {{path/to/file.hurl}}`

- Փորձարկեք HTTP հարցումները ֆայլից և ստեղծեք հաշվետվություն HTML-ով.:

`hurl --test --report-html {{path/to/output_directory}} {{path/to/file.hurl}}`
