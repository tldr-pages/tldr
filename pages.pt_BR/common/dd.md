# dd

> Converte e copia um arquivo.
> Mais informações: <https://manned.org/dd.1p>.

- Cria um dispositivo USB inicializável a partir de um arquivo isohybrid (tal como `archlinux-xxx.iso`) e mostra o progresso:

`dd if={{caminho/para/arquivo.iso}} of={{/dev/dispositivo_usb}} status=progress`

- Clona um dispositivo para outro dispositivo com bloco de 4 MiB e descarta escritas antes que o comando termine:

`dd bs=4194304 conv=fsync if={{/dev/dispositivo_origem}} of={{/dev/dispositivo_destino}}`

- Gera um arquivo com um número específico de bytes aleatórios utilizando o driver random do kernel:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{caminho/para/arquivo_aleatório}}`

- Faz análise do desempenho da escrita sequencial de um disco:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{caminho/para/arquivo_1GB}}`

- Cria um backup do sistema, salva-o em arquivo IMG (pode ser restaurado posteriormente trocando `if` e `of`) e mostra o progresso:

`dd if={{/dev/dispositivo}} of={{caminho/para/arquivo.img}} status=progress`
