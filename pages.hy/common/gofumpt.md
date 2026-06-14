#խայտառակություն

> Խստորեն ձևաչափեք Go ֆայլերը:.
> Տես նաև՝ `gofmt`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mvdan/gofumpt#gofumpt>:.

- Ձևաչափեք Go ֆայլերը.:

`gofumpt -w {{path/to/directory}}`

- [l]ցուցակ ֆայլեր, որոնց ֆորմատավորումը տարբերվում է `gofumpt`-ից.:

`gofumpt -l {{path/to/directory}}`

- Հաղորդել բոլոր [e]սխալների մասին.:

`gofumpt -e {{path/to/directory}}`

- Ցուցադրել [d]ifs:

`gofumpt -d {{path/to/directory}}`

- Ձևաչափեք Go ֆայլերը ավելի խիստ կանոններով.:

`gofumpt -extra {{path/to/directory}}`

- Ցուցադրել [d]iffs ավելի խիստ կանոններով.:

`gofumpt -extra -d {{path/to/directory}}`

- Ցուցադրել օգնությունը.:

`gofumpt {{[-h|--help]}}`
