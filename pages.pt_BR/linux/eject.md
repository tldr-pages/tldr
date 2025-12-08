# eject

> Ejeta CDs, disquetes, unidades de fita e dispositivos USB.
> Mais informações: <https://manned.org/eject>.

- Exibir o dispositivo padrão:

`eject {{[-d|--default]}}`

- Ejetar o dispositivo padrão:

`eject`

- Ejetar um dispositivo específico (a ordem padrão é: cd-rom, scsi, disquete e fita):

`eject {{/dev/cdrom}}`

- Alternar o estado da bandeja de um dispositivo (abrir/fechar):

`eject {{[-T|--traytoggle]}} {{/dev/cdrom}}`

- Ejetar uma unidade de CD:

`eject {{[-r|--cdrom]}} {{/dev/cdrom}}`

- Ejetar uma unidade de disquete:
`eject {{[-f|--floppy]}} {{/mnt/floppy}}`

- Ejetar uma unidade de fita:

`eject {{[-q|--tape]}} {{/mnt/tape}}`

- Definir se o botão de ejeção físico é [i]gnorado (`on` impede a ejeção):

`eject {{[-i|--manualeject]}} {{on|off}}`
