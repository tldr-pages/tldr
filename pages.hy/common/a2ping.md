# a2ping

> Փոխակերպեք պատկերները EPS կամ PDF ֆայլերի:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/a2ping>:.

- Պատկերը փոխարկեք PDF-ի (Նշում. ելքային ֆայլի անունը նշելը պարտադիր չէ).:

`a2ping {{path/to/image.ext}} {{path/to/output.pdf}}`

- Սեղմեք փաստաթուղթը նշված մեթոդով.:

`a2ping --nocompress {{none|zip|best|flate}} {{path/to/file}}`

- Սկանավորեք HiResBoundingBox-ը, եթե առկա է (կանխադրված՝ այո):

`a2ping --nohires {{path/to/file}}`

- Թույլատրել էջի բովանդակությունը սկզբնաղբյուրից ներքևում և ձախից (կանխադրված է ոչ):

`a2ping --below {{path/to/file}}`

- Լրացուցիչ փաստարկներ փոխանցեք `gs`-ին:

`a2ping --gsextra {{arguments}} {{path/to/file}}`

- Լրացուցիչ փաստարկներ փոխանցեք արտաքին ծրագրին (այսինքն `pdftops`):

`a2ping --extra {{arguments}} {{path/to/file}}`

- Ցուցադրել օգնությունը.:

`a2ping {{[-h|--help]}}`
