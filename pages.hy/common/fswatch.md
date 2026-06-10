# fswatch

> Ֆայլերի փոփոխման միջպլատֆորմային մոնիտոր:.
> Լրացուցիչ տեղեկություններ. <https://emcrisostomo.github.io/fswatch/>:.

- Գործարկեք Bash հրամանը ֆայլի ստեղծման, թարմացման կամ ջնջման ժամանակ.:

`fswatch {{path/to/file}} | xargs {{[-n|--max-args]}} 1 {{bash_command}}`

- Դիտեք մեկ կամ ավելի ֆայլեր և/կամ գրացուցակներ.:

`fswatch {{path/to/file}} {{path/to/directory}} {{path/to/another_directory/**/*.js}} | xargs {{[-n|--max-args]}} 1 {{bash_command}}`

- Տպեք փոխված ֆայլերի բացարձակ ուղիները.:

`fswatch {{path/to/directory}} | xargs {{[-n|--max-args]}} 1 -I _ echo _`

- Զտել ըստ իրադարձության տեսակի.:

`fswatch --event {{Updated|Removed|Created|...}} {{path/to/directory}} | xargs {{[-n|--max-args]}} 1 {{bash_command}}`
