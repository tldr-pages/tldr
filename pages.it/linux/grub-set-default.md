# grub-set-default

> Imposta la voce di avvio predefinita per GRUB.
> Maggiori informazioni: <https://manned.org/grub-set-default>.

- Imposta la voce di avvio predefinita su un numero, nome o identificatore:

`sudo grub-set-default {{numero_entry}}`

- Imposta la voce di avvio predefinita su un numero, nome o identificatore per una directory di avvio alternativa:

`sudo grub-set-default --boot-directory /{{percorso/della/cartella_boot}} {{numero_entry}}`
