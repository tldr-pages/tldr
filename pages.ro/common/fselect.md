# fselect

> Găsiți fișiere cu interogări asemănătoare SQL.
> Mai multe informaţii: <https://github.com/jhspetersson/fselect>

- Selectați calea și dimensiunea completă din fișierele temporare sau de configurare dintr-un anumit director:

`fselect size, path from {{path/to/directory}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}`

- Găsiți imagini pătrate:

`fselect path from {{path/to/directory}} where width = height`

- Găsiți vechi de școală rap 320kbps fișiere MP3:

`fselect path from {{path/to/directory}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}`

- Selectați doar primele 5 rezultate și de ieșire ca JSON:

`fselect size, path from {{path/to/directory}} limit {{5}} into json`

- Utilizați funcțiile agregate SQL pentru a calcula dimensiunea minimă, maximă și medie a fișierelor într-un director:

`fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{path/to/directory}}"`
