# sysbench

> Համակարգի պրոցեսորի, IO-ի և հիշողության չափորոշիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/akopytov/sysbench#usage>:.

- Գործարկեք պրոցեսորի հենանիշը 1 շղթայով 10 վայրկյան.:

`sysbench cpu run`

- Գործարկեք CPU-ի չափանիշը մի քանի թելերով որոշակի ժամանակով.:

`sysbench --threads={{number_of_threads}} --time={{seconds}}`

- Գործարկել հիշողության չափանիշը 1 շղթայով 10 վայրկյան.:

`sysbench memory run`

- Պատրաստեք ֆայլային համակարգի մակարդակի ընթերցման չափանիշ.:

`sysbench fileio prepare`

- Գործարկել ֆայլային համակարգի մակարդակի չափանիշ.:

`sysbench --file-test-mode={{rndrd|rndrw|rndwr|seqrd|seqrewr|seqwr}} fileio run`
