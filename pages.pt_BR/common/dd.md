# dd

> Converte e copia um arquivo.
> Mais informações: <https://manned.org/man/dd.1p>.

- Cria um USB drive bootável a partir de um arquivo isohybrid (como uma archlinux-xxx.iso) e mostra o progresso:

`dd if={{arquivo.iso}} of=/dev/{{usb_drive}} status=progress`

- Clona um drive para outro drive com 4 MiB block, ignora erros e mostra o progresso:

`dd if=/dev/{{drive_fonte}} of=/dev/{{drive_destino}} bs=4M conv=noerror status=progress`

- Gera um arquivo com 100 bytes aleatórios utilizando o kernel random driver:

`dd if=/dev/urandom of={{arquivo_random}} bs=100 count=1`

- Faz o benchmark da performance de escrita de um disco:

`dd if=/dev/zero of={{arquivo_1GB}} bs=1024 count=1000000`

- Gera um backup do sistema em um arquivo IMG e mostra o progresso:

`dd if=/dev/{{dispositivo_drive}} of={{caminho/para/arquivo.img}} status=progress`

- Restaura um drive a partir de um arquivo IMG e mostra o progresso:

`dd if={{caminho/para/arquivo.img}} of=/dev/{{dispositivo_drive}} status=progress`

- Checa o progresso de um processo `dd` rodando (rode esse comando de outro shell):

`kill -USR1 $(pgrep -x dd)`
