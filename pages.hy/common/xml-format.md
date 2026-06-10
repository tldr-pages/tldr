# xml ձևաչափ

> Ձևաչափեք XML փաստաթուղթը:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139569312>:.

- Ձևաչափեք XML փաստաթուղթը՝ ներդիրներով ներդիրով.:

`xml {{[fo|format]}} {{[-t|--indent-tab]}} {{path/to/input.xml|uri}} > {{path/to/output.xml}}`

- Ձևաչափեք HTML փաստաթուղթ՝ 4 բացատներով.:

`xml {{[fo|format]}} {{[-H|--html]}} {{[-s|--indent-spaces]}} {{4}} {{path/to/input.html|uri}} > {{path/to/output.html}}`

- Վերականգնել սխալ ձևավորված XML փաստաթղթի վերլուծելի մասերը, առանց նահանջի.:

`xml {{[fo|format]}} {{[-R|--recover]}} {{[-n|--noindent]}} {{path/to/malformed.xml|uri}} > {{path/to/recovered.xml}}`

- Ձևաչափեք XML փաստաթուղթը `stdin`-ից՝ հեռացնելով `DOCTYPE` հայտարարությունը.:

`cat {{path/to/input.xml}} | xml {{[fo|format]}} {{[-D|--dropdtd]}} > {{path/to/output.xml}}`

- Ձևաչափեք XML փաստաթուղթը՝ բաց թողնելով XML հայտարարությունը.:

`xml {{[fo|format]}} {{[-o|--omit-decl]}} {{path/to/input.xml|uri}} > {{path/to/output.xml}}`

- Ցուցադրել օգնությունը.:

`xml {{[fo|format]}} --help`
