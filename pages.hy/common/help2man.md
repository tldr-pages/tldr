# help2man

> Ստեղծեք պարզ մարդ էջեր գործարկվող `--help` և `--version` ելքից:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/help2man/#Invoking-help2man>:.

- Ստեղծեք մարդ էջ գործարկվողի համար.:

`help2man {{executable}}`

- Տղամարդու էջում նշեք «անուն» պարբերությունը.:

`help2man {{executable}} {{[-n|--name]}} {{name}}`

- Նշեք մարդ էջի բաժինը (կանխադրված է 1):

`help2man {{executable}} {{[-s|--section]}} {{section}}`

- Արդյունք ֆայլ՝ `stdout`-ի փոխարեն:

`help2man {{executable}} {{[-o|--output]}} {{path/to/file}}`

- Ցուցադրել օգնությունը.:

`help2man --help`
