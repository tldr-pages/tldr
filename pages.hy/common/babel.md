#բաբելոն

> Տրանսպիլյատոր, որը փոխակերպում է կոդը JavaScript ES6/ES7 շարահյուսությունից ES5 շարահյուսության:.
> Լրացուցիչ տեղեկություններ. <https://babeljs.io/docs/babel-cli>:.

- Տեղափոխեք նշված մուտքային ֆայլը և թողարկեք `stdout`:

`babel {{path/to/file}}`

- Փոխանցել նշված մուտքային ֆայլը և ելքը որոշակի ֆայլի.:

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Տեղափոխեք մուտքագրված ֆայլը ամեն անգամ, երբ այն փոխվում է.:

`babel {{path/to/input_file}} --watch`

- Փոխակերպել ֆայլերի մի ամբողջ գրացուցակ.:

`babel {{path/to/input_directory}}`

- Անտեսեք ստորակետերով առանձնացված ֆայլերը գրացուցակում.:

`babel {{path/to/input_directory}} --ignore {{ignored_file1,ignored_file2,...}}`

- Տեղափոխել և թողարկել որպես նվազագույն JavaScript.:

`babel {{path/to/input_file}} --minified`

- Ընտրեք մի շարք նախադրյալներ ելքային ձևաչափման համար.:

`babel {{path/to/input_file}} --presets {{preset1,preset2,...}}`

- Ցուցադրել օգնությունը.:

`babel --help`
