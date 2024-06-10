# dd

> Converte e copia um arquivo.
> Mais informações: <https://manned.org/man/dd.1p>.

- Cria um USB drive bootável a partir de um arquivo isohybrid (como uma `archlinux-xxx.iso`):

`dd if={{caminho/para/arquivo.iso}} of={{/dev/usb_drive}}`

- Clona um drive para outro drive com 4 MiB block e ignora erros:

`dd bs=4194304 conv=noerror if={{/dev/drive_fonte}} of={{/dev/drive_destino}}`

- Gera um arquivo com um número específico de bytes aleatórios utilizando o kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{caminho/para/arquivo_random}}`

- Faz o benchmark da performance de escrita de um disco:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{caminho/para/arquivo_1GB}}`

- Gera um backup do sistema em um arquivo IMG e mostra o progresso:

`dd if={{/dev/dispositivo_drive}} of={{caminho/para/arquivo.img}} status=progress`
