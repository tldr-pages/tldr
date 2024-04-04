# diskutil

> Utilitário para gerenciar discos e volumes locais.
> Mais informações: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Lista todos os discos, partições, e volumes montados atualmente disponíveis:

`diskutil list`

- Repara as estruturas de dados do sistema de arquivos de um volume:

`diskutil repairVolume {{/dev/diskX}}`

- Desmonta um volume:

`diskutil unmountDisk {{/dev/diskX}}`

- Ejeta um CD/DVD (desmonta primeiro):

`diskutil eject {{/dev/disk1}}`
