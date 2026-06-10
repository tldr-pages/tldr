# սդ

> Ինտուիտիվ գտնել և փոխարինել:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sd>:.

- Կտրեք որոշ բացատներ՝ օգտագործելով `regex` (ելքային հոսք՝ `stdout`):

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- Փոխարինեք բառերը՝ օգտագործելով նկարահանման խմբեր (ելքային հոսք՝ `stdout`):

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Գտեք և փոխարինեք որոշակի ֆայլում (ելքային հոսք՝ `stdout`):

`sd {{[-p|--preview]}} '{{window.fetch}}' '{{fetch}}' {{path/to/file.js}}`

- Գտեք և փոխարինեք ընթացիկ նախագծի բոլոր ֆայլերում.:

`find . -type f -exec sd '{{from "react"}}' '{{from "preact"}}' {} \;`
