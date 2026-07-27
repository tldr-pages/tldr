# grub-probe

> Analizza le informazioni del dispositivo per un percorso o dispositivo particolare.
> Maggiori informazioni: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dprobe.html>.

- Ottiene il modulo filesystem GRUB per un percorso:

`sudo grub-probe {{[-t|--target]}} fs {{/boot/grub}}`

- Ottiene il dispositivo di sistema che contiene un percorso:

`sudo grub-probe {{[-t|--target]}} device {{/boot/grub}}`

- Ottiene il nome del disco GRUB per un dispositivo di sistema:

`sudo grub-probe {{[-t|--target]}} drive {{/dev/sdX}} {{[-d|--device]}}`

- Ottiene l'UUID del filesystem:

`sudo grub-probe {{[-t|--target]}} fs_uuid {{/boot/grub}}`

- Ottiene l'etichetta del filesystem:

`sudo grub-probe {{[-t|--target]}} fs_label {{/boot/grub}}`

- Ottiene il codice del tipo di partizione MBR (due cifre esadecimali):

`sudo grub-probe {{[-t|--target]}} msdos_parttype {{/dev/sdX}}`

- Analizza usando una mappa dispositivi personalizzata:

`sudo grub-probe {{[-t|--target]}} drive {{/boot/grub}} {{[-m|--device-map]}} {{path/to/custom_device.map}}`
