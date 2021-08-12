# history expansion

> Reutilizați și extindeți istoricul shell în `sh`, `bash`, `zsh`, `rbash` și `ksh`.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>

- Rulați comanda anterioară ca root (`!! `se înlocuieşte cu comanda anterioară):

`sudo !!`

- Rulați o comandă cu ultimul argument al comenzii anterioare:

`{{command}} !$`

- Rulați o comandă cu primul argument al comenzii anterioare:

`{{command}} !^`

- Rulează comanda Nth a istoriei:

`!{{n}}`

- Rulați liniile de comandă `n `înapoi în istorie:

`!-{{n}}`

- Rulați cea mai recentă comandă care conține `string':

`!?{{string}}?`

- Rulați comanda anterioară, înlocuind `string1` cu `string2`:

`^{{string1}}^{{string2}}^`

- Efectuați o extindere a istoricului, dar imprimați comanda care ar fi rulată în loc să o rulați efectiv:

`{{!-n}}:p`
