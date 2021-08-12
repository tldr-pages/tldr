# enca

> Detectați și convertiți codificarea fișierelor text.
> Mai multe informaţii: <https://github.com/nijel/enca>

- Detectează codificarea fişierelor în funcţie de setările regionale ale sistemului:

`enca {{file1 file2 ...}}`

- Detectați codificarea fișierului (fișierelor) specificând o limbă în formatul local POSIX/C (de exemplu, ZH_CN, EN_US):

`enca -L {{language}} {{file1 file2 ...}}`

- Conversia fișierului (fișierelor) într-o codificare specifică:

`enca -L {{language}} -x {{to_encoding}} {{file1 file2 ...}}`

- Creați o copie a unui fișier existent utilizând o codificare diferită:

`enca -L {{language}} -x {{to_encoding}}  <{{original_file}}> {{new_file}}`
