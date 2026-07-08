# grub-set-default

> Imposta la voce di avvio predefinita per GRUB.
> Maggiori informazioni: <https://manned.org/grub-set-default>.

- Imposta la voce di avvio predefinita su un numero, nome o identificatore:

`sudo grub-set-default {{entry_number}}`

- Imposta la voce di avvio predefinita su un numero, nome o identificatore per una directory di avvio alternativa:

`sudo grub-set-default --boot-directory /{{path/to/boot_directory}} {{entry_number}}`
