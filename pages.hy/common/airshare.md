# օդային բաժնետոմս

> Տվյալների փոխանցում երկու մեքենաների միջև տեղական ցանցում:.
> Լրացուցիչ տեղեկություններ. <https://airshare.readthedocs.io/en/latest/cli.html>:.

- Համօգտագործեք ֆայլեր կամ գրացուցակներ.:

`airshare {{code}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ստացեք ֆայլ.:

`airshare {{code}}`

- Հյուրընկալեք ստացող սերվեր (օգտագործեք սա, որպեսզի կարողանաք ֆայլեր վերբեռնել վեբ ինտերֆեյսի միջոցով).:

`airshare --upload {{code}}`

- Ուղարկեք ֆայլեր կամ գրացուցակներ ստացող սերվեր.:

`airshare --upload {{code}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ուղարկեք ֆայլեր, որոնց ուղիները պատճենվել են clipboard.:

`airshare --file-path {{code}}`

- Ստացեք ֆայլ և պատճենեք այն clipboard-ում.:

`airshare --clip-receive {{code}}`
