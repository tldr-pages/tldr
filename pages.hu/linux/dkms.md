# dkms

> Egy keretrendszer, amely lehetővé teszi a kernelmodulok dinamikus felépítését. További információ: <https://github.com/dell/dkms>.

- A jelenleg telepített modulok listája:

`dkms status`

- Újraépíti az összes modult az aktuálisan futó rendszermaghoz:

`dkms autoinstall`

- Az acpi_call modul 1.2.1-es verziójának telepítése a jelenleg futó rendszermaghoz:

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- Az acpi_call modul 1.2.1-es verziójának eltávolítása az összes rendszermagból:

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
