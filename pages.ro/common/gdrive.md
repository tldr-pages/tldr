# gdrive

> Instrument linie de comandă pentru a interacționa cu Google Drive.
> ID-ul dosarului/fișierului poate fi obținut din dosarul Google Drive sau din URL-ul idului.
> Mai multe informaţii: <https://github.com/gdrive-org/gdrive>

- Încărcați o cale locală în folderul părinte cu ID-ul specificat:

`gdrive upload -p {{id}} {{path/to/file_or_folder}}`

- Descărcați fișierul sau directorul după id în directorul curent:

`gdrive download {{id}}`

- Descărcați pe o cale locală dată prin id-ul său:

`gdrive download --path {{path/to/folder}} {{id}}`

- Creați o nouă revizuire a unui id utilizând un fișier sau un folder dat:

`gdrive update {{id}} {{path/to/file_or_folder}}`
