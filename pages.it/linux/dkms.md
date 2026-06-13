# dkms

> Un framework che permette la compilazione dinamica di moduli del kernel.
> Maggiori informazioni: <https://manned.org/dkms>.

- Elenca i moduli attualmente installati:

`dkms status`

- Ricompila tutti i moduli per il kernel in esecuzione:

`sudo dkms autoinstall`

- Installa la versione 1.2.1 del modulo acpi_call per il kernel in esecuzione:

`sudo dkms install -m {{acpi_call}} -v {{1.2.1}}`

- Rimuovi la versione 1.2.1 del modulo acpi_call da tutti i kernel:

`sudo dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
