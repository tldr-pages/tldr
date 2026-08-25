# qemu-system-x86_64

> Emula a arquitetura `x86_64`.
> Mais informações: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Inicializa a partir de uma imagem emulando a arquitetura `x86_64`:

`qemu-system-x86_64 -hda {{nome_da_imagem.img}} -m {{4096}}`

- Inicializa uma instância do QEMU a partir de uma imagem live ISO:

`qemu-system-x86_64 -hda {{nome_da_imagem.img}} -m {{4096}} -cdrom {{imagem_do_sistema.iso}} -boot d`

- Inicializa a partir de um dispositivo físico (ex.: a partir do USB para testar uma mídia inicializável):

`qemu-system-x86_64 -hda {{/dev/dispositivo_de_armazenamento}} -m {{4096}}`

- Não inicia um servidor VNC:

`qemu-system-x86_64 -hda {{nome_da_imagem.img}} -m {{4096}} -nographic`

- Sai do QEMU sem gráficos:

`<Ctrl a><x>`

- Lista os tipos de máquina suportados:

`qemu-system-x86_64 {{[-M|-machine]}} help`
