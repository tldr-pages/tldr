# pnmtofiasco

> Փոխարկեք PNM պատկերը սեղմված FIASCO ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtofiasco.html>:.

- Փոխակերպեք PNM պատկերը սեղմված FIASCO ֆայլի.:

`pnmtofiasco {{path/to/file.pnm}} > {{path/to/file.fiasco}}`

- Նշեք մուտքագրված ֆայլերը օրինաչափության միջոցով.:

`pnmtofiasco {{[-i|--image-name]}} "{{img[01-09+1].pnm}}" > {{path/to/file.fiasco}}`

- Նշեք սեղմման որակը.:

`pnmtofiasco {{[-q|--quality]}} {{quality_level}} {{path/to/file.pnm}} > {{path/to/file.fiasco}}`

- Բեռնել ընտրանքները, որոնք պետք է օգտագործվեն նշված կազմաձևման ֆայլից.:

`pnmtofiasco {{[-f|--config]}} {{path/to/fiascorc}} {{path/to/file.pnm}} > {{path/to/file.fiasco}}`
