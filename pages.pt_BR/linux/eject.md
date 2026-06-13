# eject

> Ejeta CDs, disquetes, unidades de fita e dispositivos USB.
> Mais informações: <https://manned.org/eject>.

- Exibe o dispositivo padrão:

`eject {{[-d|--default]}}`

- Ejeta o dispositivo padrão:

`eject`

- Ejeta um dispositivo específico (a ordem padrão é: cd-rom, scsi, disquete e fita):

`eject {{/dev/cdrom}}`

- Alterna o estado da bandeja de um dispositivo (abre/fecha):

`eject {{[-T|--traytoggle]}} {{/dev/cdrom}}`

- Ejeta uma unidade de CD:

`eject {{[-r|--cdrom]}} {{/dev/cdrom}}`

- Ejeta uma unidade de disquete:

`eject {{[-f|--floppy]}} {{/mnt/floppy}}`

- Ejeta uma unidade de fita:

`eject {{[-q|--tape]}} {{/mnt/tape}}`

- Define se o botão de ejeção físico é [i]gnorado (`on` impede a ejeção):

`eject {{[-i|--manualeject]}} {{on|off}}`
