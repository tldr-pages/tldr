# alex

> Un instrument care captează scrisul insensibil, nechibzuit.
> Vă ajută să găsiți favorizarea sexului, polarizarea, ruda rasială, religia nechibzuită sau alte fraze inegale în text.
> Mai multe informaţii: <https://github.com/get-alex/alex>

- Analizați textul din stdin:

`echo {{His network looks good}} | alex --stdin`

- Analizați toate fișierele din directorul curent:

`alex`

- Analizaţi un anumit fişier:

`alex {{textfile.md}}`

- Analizaţi toate fişierele Markdown cu excepţia `example.md`:

`alex *.md !{{example.md}}`
