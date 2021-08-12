# sdiff

> Comparați diferențele dintre și, opțional, îmbinați 2 fișiere.

- Comparați 2 fișiere:

`sdiff {{path/to/file1}} {{path/to/file2}}`

- Comparați 2 fișiere, ignorând toate filele și spațiul alb:

`sdiff -W {{path/to/file1}} {{path/to/file2}}`

- Comparați 2 fișiere, ignorând spațiul alb la sfârșitul liniilor:

`sdiff -Z {{path/to/file1}} {{path/to/file2}}`

- Comparați 2 fișiere într-o manieră insensibilă la majuscule:

`sdiff -i {{path/to/file1}} {{path/to/file2}}`

- Comparați și apoi îmbinați, scriind ieșirea într-un fișier nou:

`sdiff -o {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}`
