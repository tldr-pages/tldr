#զեկ

> Ստեղծեք Go struct XML-ից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/miku/zek#usage>:.

- Ստեղծեք Go կառուցվածքը տրված XML-ից `stdin`-ից և ցուցադրեք ելքը `stdout`-ում:

`cat {{path/to/input.xml}} | zek`

- Ստեղծեք Go կառուցվածքը տրված XML-ից `stdin`-ից և ուղարկեք արդյունքը ֆայլ.:

`curl {{[-s|--silent]}} {{https://url/to/xml}} | zek -o {{path/to/output.go}}`

- Ստեղծեք Go ծրագրի օրինակ տրված XML-ից `stdin`-ից և ուղարկեք արդյունքը ֆայլ.:

`cat {{path/to/input.xml}} | zek -p -o {{path/to/output.go}}`
