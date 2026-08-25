# qemu-img

> Cria e manipula imagens de disco virtuais do Quick Emulator.
> Mais informações: <https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- Cria uma imagem de disco com um tamanho específico (em gigabytes):

`qemu-img create {{caminho/para/arquivo_de_imagem.img}} {{gigabytes}}G`

- Mostra informações sobre uma imagem de disco:

`qemu-img info {{caminho/para/arquivo_de_imagem.img}}`

- Aumenta ou diminui o tamanho da imagem:

`qemu-img resize {{caminho/para/arquivo_de_imagem.img}} {{gigabytes}}G`

- Exibe o estado de alocação de cada setor da imagem de disco especificada:

`qemu-img map {{caminho/para/arquivo_de_imagem.img}}`

- Converte uma imagem de disco VMware `.vmdk` para uma imagem de disco `.qcow2` do KVM enquanto mostra o [p]rogresso:

`qemu-img convert -f vmdk -O qcow2 -p {{caminho/para/arquivo_de_imagem.vmdk}} {{caminho/para/arquivo_de_imagem.qcow2}}`

- [c]ria uma snapshot interna de uma imagem de disco `.qcow2` do KVM:

`qemu-img snapshot -c {{nome_da_snapshot}} {{caminho/para/arquivo_de_imagem.qcow2}}`

- [a]plica uma snapshot interna em uma imagem de disco `.qcow2` do KVM:

`qemu-img snapshot -a {{nome_da_snapshot}} {{caminho/para/arquivo_de_imagem.qcow2}}`
