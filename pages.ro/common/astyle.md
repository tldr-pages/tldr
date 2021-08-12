# astyle

> Indenter de cod sursă, formator și înfrumusețător pentru limbajele de programare C, C++, C# și Java.
> La rulare, o copie a fișierului original este creată cu un „.orig” atașat la numele fișierului original.
> Mai multe informaţii: <http://astyle.sourceforge.net/>

- Aplicați stilul implicit de 4 spații per liniuță și fără modificări de formatare:

`astyle {{source_file}}`

- Aplicați stilul Java cu bretele atașate:

`astyle --style=java {{path/to/file}}`

- Aplicați stilul allman cu bretele rupte:

`astyle --style=allman {{path/to/file}}`

- Aplicați o indentare particularizată utilizând spații. Alegeți între 2 și 20 de spații:

`astyle --indent=spaces={{number_of_spaces}} {{path/to/file}}`

- Aplicați o indentare particularizată utilizând file. Alegeți între 2 și 20 de file:

`astyle --indent=tab={{number_of_tabs}} {{path/to/file}}`
