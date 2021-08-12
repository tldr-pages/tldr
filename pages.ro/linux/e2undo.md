# e2undo

> Replay anulare jurnalele pentru un sistem de fișiere ext2/ext3/ext4.
> Acest lucru poate fi utilizat pentru a anula o operațiune eșuată de un program e2fsprogs.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/e2undo.8.html>

- Afișați informații despre un anumit fișier de anulare:

`e2undo -h {{path/to/undo_file}} {{/dev/sdXN}}`

- Efectuați o alergare uscată și afișați blocurile candidate pentru reluarea:

`e2undo -nv {{path/to/undo_file}} {{/dev/sdXN}}`

- Efectuați o operație de anulare:

`e2undo {{path/to/undo_file}} {{/dev/sdXN}}`

- Efectuați o operațiune de anulare și afișați informații detaliate:

`e2undo -v {{path/to/undo_file}} {{/dev/sdXN}}`

- Scrieți conținutul vechi al blocului într-un fișier anulare înainte de a suprascrie un bloc de sistem de fișiere:

`e2undo -z {{path/to/file.e2undo}} {{path/to/undo_file}} {{/dev/sdXN}}`
