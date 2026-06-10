# json5

> Փոխարկեք JSON5 ֆայլերը JSON-ի:.
> Լրացուցիչ տեղեկություններ. <https://json5.org/#cli>:.

- Փոխարկել JSON5 `stdin`-ը JSON `stdout`:

`echo {{input}} | json5`

- Փոխակերպեք JSON5 ֆայլը JSON և թողարկեք `stdout`:

`json5 {{path/to/input_file.json5}}`

- Փոխակերպեք JSON5 ֆայլը նշված JSON ֆայլին.:

`json5 {{path/to/input_file.json5}} {{[-o|--out-file]}} {{path/to/output_file.json}}`

- Վավերացրեք JSON5 ֆայլը.:

`json5 {{path/to/input_file.json5}} {{[-v|--validate]}}`

- Նշեք բացատների քանակը, որոնք պետք է ներդիրների համար (կամ «t») մատնանշվեն.:

`json5 {{[-s|--space]}} {{indent_amount}}`

- Ցուցադրել օգնությունը.:

`json5 {{[-h|--help]}}`
