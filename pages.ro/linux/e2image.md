# e2image

> Salvați metadatele critice ale sistemului de fișiere ext2/ext3/ext4 într-un fișier.
> Mai multe informaţii: <https://manned.org/e2image>

- Scrie metadate amplasate pe dispozitiv într-un anumit fișier:

`e2image {{/dev/sdXN}} {{path/to/image_file}}`

- Imprimare metadate localizate pe dispozitiv la stdout:

`e2image {{/dev/sdXN}} -`

- Restaurați metadatele sistemului de fișiere înapoi pe dispozitiv:

`e2image -I {{/dev/sdXN}} {{path/to/image_file}}`

- Creați un fișier rar brut mare cu metadate la offsets corespunzătoare:

`e2image -r {{/dev/sdXN}} {{path/to/image_file}}`

- Creați un fișier imagine QCOW2 în locul unui fișier imagine normal sau brut:

`e2image -Q {{/dev/sdXN}} {{path/to/image_file}}`
