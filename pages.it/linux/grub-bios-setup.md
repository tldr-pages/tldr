# grub-bios-setup

> Configura un dispositivo per usare GRUB con una configurazione BIOS.
> Dovresti usare `grub-install` invece di `grub-bios-setup` nella maggior parte dei casi.
> Maggiori informazioni: <https://manned.org/grub-bios-setup>.

- Configura un dispositivo per l'avvio con GRUB:

`grub-bios-setup {{/dev/sdX}}`

- Installa anche se vengono rilevati problemi:

`grub-bios-setup {{[-f|--force]}} {{/dev/sdX}}`

- Installa GRUB in una directory specifica:

`grub-bios-setup {{[-d|--directory]}} {{/boot/grub}} {{/dev/sdX}}`
