# grub-reboot

> Imposta la voce di avvio predefinita per GRUB, solo per il prossimo avvio.
> Maggiori informazioni: <https://manned.org/grub-reboot>.

- Imposta la voce di avvio predefinita su un numero, nome o identificatore per il prossimo avvio:

`sudo grub-reboot {{entry_number}}`

- Imposta la voce di avvio predefinita su un numero, nome o identificatore per una directory di avvio alternativa per il prossimo avvio:

`sudo grub-reboot --boot-directory /{{path/to/boot_directory}} {{entry_number}}`
