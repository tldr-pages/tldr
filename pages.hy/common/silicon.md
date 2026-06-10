#սիլիկոն

> Ստեղծեք սկզբնական կոդի պատկեր:.
> Տես նաև՝ `freeze`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Aloxaf/silicon#examples>:.

- Ստեղծեք պատկեր որոշակի աղբյուրի ֆայլից.:

`silicon {{path/to/source_file}} {{[-o|--output]}} {{path/to/output_image}}`

- Ստեղծեք պատկեր աղբյուրի ֆայլից՝ հատուկ ծրագրավորման լեզվի շարահյուսության ընդգծմամբ (օրինակ՝ `rust`, `py`, `js` և այլն):

`silicon {{path/to/source_file}} {{[-o|--output]}} {{path/to/output_image}} {{[-l|--language]}} {{language|extension}}`

- Ստեղծեք պատկեր `stdin`-ից:

`{{command}} | silicon {{[-o|--output]}} {{path/to/output_image}}`
