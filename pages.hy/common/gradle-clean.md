# gradle մաքուր

> Ջնջել կառուցման գրացուցակը և բոլոր ստեղծված ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/command_line_interface.html#cleaning_outputs>:.

- Մաքրել կառուցման գրացուցակը.:

`gradle clean`

- Մաքրեք և այնուհետև կառուցեք նախագիծը.:

`gradle clean build`

- Մաքրել կոնկրետ ենթածրագիր բազմաբնույթ նախագծի կառուցման մեջ.:

`gradle :{{subproject}}:clean`

- Մաքրել ավելի մանրամասն հատումներով.:

`gradle clean {{[-i|--info]}}`
