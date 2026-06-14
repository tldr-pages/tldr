# ecpg

> Ներկառուցված SQL նախապրոցեսոր C ծրագրերի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-ecpg.html>:.

- Նախամշակեք որոշակի ֆայլ.:

`ecpg {{input.pgc}}`

- Նախամշակում `stdin`-ից և թողարկում `stdout`:

`ecpg -o - -`

- Նախապես մշակեք `stdin`-ից և գրեք ֆայլում՝:

`cat input.pgc | ecpg -o output.c -`

- Նախամշակեք և նշեք ելքային ֆայլ.:

`ecpg -o {{output.c}} {{input.pgc}}`

- Նախամշակեք վերնագրի ֆայլը (`.pgh` ընդլայնում).:

`ecpg {{input.pgh}}`

- Նախամշակում հատուկ համատեղելիության ռեժիմով.:

`ecpg -C {{INFORMIX|INFORMIX_SE|ORACLE}} {{input.pgc}}`

- Նախամշակում` միացված ավտոմատ կերպով.:

`ecpg -t {{input.pgc}}`
