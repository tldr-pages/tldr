# diffoscope

> Comparați fișiere, arhive și directoare.
> Mai multe informaţii: <https://diffoscope.org>

- Comparați două fișiere:

`diffoscope {{path/to/file1}} {{path/to/file2}}`

- Comparați două fișiere fără a afișa o bară de progres:

`diffoscope --no-progress {{path/to/file1}} {{path/to/file2}}`

- Comparați două fișiere și scrieți un raport HTML într-un fișier (utilizați `-` pentru stdout):

`diffoscope --html {{path/to/outfile|-}} {{path/to/file1}} {{path/to/file2}}`

- Comparați două directoare cu excepția fișierelor cu un nume care se potrivește cu un model specificat:

`diffoscope --exclude {{pattern}} {{path/to/directory1}} {{path/to/directory2}}`

- Comparați două directoare și controlați dacă metadatele directorului sunt considerate:

`diffoscope --exclude-directory-metadata {{auto|yes|no|recursive}} {{path/to/directory1}} {{path/to/directory2}}`
