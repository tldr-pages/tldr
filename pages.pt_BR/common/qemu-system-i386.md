# qemu-system-i386

> Emula a arquitetura `i386`.
> Mais informações: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Inicializa a partir de uma imagem emulando a arquitetura `i386`:

`qemu-system-i386 -hda {{nome_da_imagem.img}} -m {{4096}}`

- Inicializa uma instância do QEMU a partir de uma imagem live ISO:

`qemu-system-i386 -hda {{nome_da_imagem.img}} -m {{4096}} -cdrom {{imagem_do_sistema.iso}} -boot d`

- Inicializa a partir de um dispositivo físico (ex.: a partir do USB para testar uma mídia inicializável):

`qemu-system-i386 -hda {{/dev/dispositivo_de_armazenamento}} -m {{4096}}`

- Não inicia um servidor VNC:

`qemu-system-i386 -hda {{nome_da_imagem.img}} -m {{4096}} -nographic`

- Sai do QEMU sem gráficos:

`<Ctrl a><x>`

- Lista os tipos de máquina suportados:

`qemu-system-i386 {{[-M|-machine]}} help`
