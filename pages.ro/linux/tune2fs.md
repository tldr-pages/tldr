# tune2fs

> Ajustați parametrii unui sistem de fișiere ext2, ext3 sau ext4.
> Poate fi utilizat pe sistemele de fișiere montate.
> Mai multe informaţii: <https://manned.org/tune2fs>

- Setați numărul maxim de numere înainte ca un sistem de fișiere să fie bifat la 2:

`tune2fs -c {{2}} {{/dev/sdXN}}`

- Setați eticheta sistemului de fișiere la MY_LABEL:

`tune2fs -L {{'MY_LABEL'}} {{/dev/sdXN}}`

- Activează atributele extinse și specificate de utilizator pentru un sistem de fișiere:

`tune2fs -o {{discard,user_xattr}} {{/dev/sdXN}}`

- Activează jurnalizarea pentru un sistem de fișiere:

`tune2fs -o^{{nobarrier}} {{/dev/sdXN}}`
