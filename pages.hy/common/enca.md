# enca

> Հայտնաբերել և վերափոխել տեքստային ֆայլերի կոդավորումը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/enca>:.

- Հայտնաբերել ֆայլ(ներ)ի կոդավորումը` ըստ համակարգի տեղանքի.:

`enca {{path/to/file1 path/to/file2 ...}}`

- Հայտնաբերել ֆայլ(ներ) կոդավորումը, որը նշում է լեզու POSIX/C տեղային ձևաչափով (օրինակ՝ zh_CN, en_US):

`enca {{[-L|--language]}} {{language}} {{path/to/file1 path/to/file2 ...}}`

- Փոխարկել ֆայլ(ներ)ը որոշակի կոդավորման.:

`enca {{[-L|--language]}} {{language}} {{[-x|--convert-to]}} {{to_encoding}} {{path/to/file1 path/to/file2 ...}}`

- Ստեղծեք գոյություն ունեցող ֆայլի պատճեն՝ օգտագործելով այլ կոդավորում.:

`enca < {{original_file}} {{[-L|--language]}} {{language}} {{[-x|--convert-to]}} {{to_encoding}} > {{new_file}}`
