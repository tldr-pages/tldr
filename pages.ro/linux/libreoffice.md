# libreoffice

> CLI pentru suita de birou puternică și gratuită LibreOffice.
> Mai multe informaţii: <https://www.libreoffice.org/>

- Deschideți o listă de fișiere separate de spațiu în modul doar în citire:

`libreoffice --view {{path/to/file1}} {{path/to/file2}}`

- Afișează conținutul anumitor fișiere:

`libreoffice --cat {{path/to/file1}} {{path/to/file2}}`

- Imprimați fișiere la o anumită imprimantă:

`libreoffice --pt {{printer_name}} {{path/to/file1}} {{path/to/file2}}`

- Convertiți toate fișierele `.doc` din directorul curent în pdf:

`libreoffice --convert-to {{pdf}} {{*.doc}}`
