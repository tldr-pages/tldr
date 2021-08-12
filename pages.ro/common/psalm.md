# psalm

> Un instrument de analiză statică pentru găsirea erorilor în aplicațiile PHP.
> Mai multe informaţii: <https://psalm.dev>

- Generează o configurație Psalm:

`psalm --init`

- Analizaţi directorul de lucru curent:

`psalm`

- Analizează un anumit director sau fișier:

`psalm {{path/to/file_or_directory}}`

- Analizați un proiect cu un fișier de configurare specific:

`psalm --config {{path/to/psalm.xml}}`

- Includeți constatările informaționale în ieșire:

`psalm --show-info`

- Analizarea unui proiect și afișarea statisticilor:

`psalm --stats`

- Analizaţi un proiect în paralel cu 4 fire:

`psalm --threads {{4}}`
