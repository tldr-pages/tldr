# compsize

> Calculați raportul de compresie al unui set de fișiere dintr-un sistem de fișiere Btrfs.
> A se vedea, de asemenea, `sistem de fișiere btrfs 'pentru a comprima un fișier prin defragmentarea acestuia.
> Mai multe informaţii: <https://github.com/kilobyte/compsize>

- Calculați raportul de compresie curent pentru un fișier sau director:

`sudo compsize {{path/to/file_or_directory}}`

- Nu traversați limitele sistemului de fișiere:

`sudo compsize --one-file-system {{path/to/file_or_directory}}`

- Afișați numărul de octeți brute în loc de dimensiuni care pot fi citite de om:

`sudo compsize --bytes {{path/to/file_or_directory}}`
