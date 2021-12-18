# msiexec

> Memasang, memperbarui, memperbaiki, atau menghapus program Windows melalui file MSI dan MSP yang tersedia.
> Informasi lebih lanjut: <https://docs.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Memasang sebuah program melalui file MSI:

`msiexec /package {{jalan/menuju/file.msi}}`

- Memasang file MSI dari internet:

`msiexec /package {{https://example.com/installer.msi}}`

- Memasang pembaruan program melalui file MSP:

`msiexec /update {{jalan/menuju/file.msp}}`

- Menghapus pemasangan atau pembaruan program melalui file MSI atau MSP yang tersedia:

`msiexec /uninstall {{jalan/menuju/file}}`
