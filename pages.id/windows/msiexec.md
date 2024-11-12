# msiexec

> Pasang, perbarui, perbaiki, atau hapus program Windows melalui berkas MSI dan MSP yang tersedia.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Pasang suatu program melalui berkas MSI:

`msiexec /package {{jalan\menuju\berkas.msi}}`

- Pasang berkas MSI dari suatu situs web:

`msiexec /package {{https://example.com/installer.msi}}`

- Pasang pembaruan suatu program melalui suatu berkas MSP:

`msiexec /update {{jalan\menuju\berkas.msp}}`

- Menghapus pemasangan atau pembaruan suatu program melalui file MSI atau MSP yang tersedia:

`msiexec /uninstall {{jalan\menuju\berkas}}`
