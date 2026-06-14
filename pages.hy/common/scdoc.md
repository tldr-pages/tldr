# scdoc

> Ստեղծեք `man` ձեռնարկի էջեր:.
> Լրացուցիչ տեղեկություններ. <https://git.sr.ht/~sircmpwn/scdoc/tree/master/item/scdoc.1.scd>:.

- Ստեղծեք մարդ էջեր scdoc (`.scd`) ֆայլից.:

`scdoc < {{path/to/file.scd}} > {{path/to/file.1}}`

- Ստեղծեք man էջեր scdoc ֆայլից և ցուցադրեք ստեղծված troff (man) աղբյուրը.:

`scdoc < {{path/to/file.scd}} | {{less}}`
