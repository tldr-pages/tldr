# dkms

> Un cadru care permite construirea dinamică a modulelor kernel.
> Mai multe informaţii: <https://github.com/dell/dkms>

- Lista modulelor instalate în prezent:

`dkms status`

- Reconstruiți toate modulele pentru kernel-ul care rulează în prezent:

`dkms autoinstall`

- Instalați versiunea 1.2.1 a modulului acpi_call pentru kernel-ul care rulează în prezent:

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- Eliminați versiunea 1.2.1 a modulului acpi_call din toate kernelurile:

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
