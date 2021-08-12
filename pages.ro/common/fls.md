# fls

> Listați fișiere și directoare într-un fișier imagine sau dispozitiv.
> Mai multe informaţii: <https://wiki.sleuthkit.org/index.php?title=Fls>

- Construiește o listă de fls recursivă pe un dispozitiv, căile de ieșire vor începe cu C:

`fls -r -m {{C:}} {{/dev/loop1p1}}`

- Analizați o singură partiție, oferind decalajul sectorului la care începe sistemul de fișiere din imagine:

`fls -r -m {{C:}} -o {{sector}} {{path/to/image_file}}`

- Analizați o singură partiție, oferind fusul orar al sistemului original:

`fls -r -m {{C:}} -z {{timezone}} {{/dev/loop1p1}}`
