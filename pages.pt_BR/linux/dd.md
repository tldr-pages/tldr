# dd

> Converte e copia um arquivo.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- Cria um dispositivo USB inicializável a partir de um arquivo isohybrid (como `archlinux-xxx.iso`), e mostra o progresso:

`dd if={{caminho/para/arquivo.iso}} of={{/dev/dispositivo_usb}} status=progress`

- Clona um dispositivo para outro dispositivo com blocos de 4MiB e salva em disco antes de o comando finalizar a execução:

`dd bs=4M conv=fsync if={{/dev/dispositivo_de_origem}} of={{/dev/dispositivo_de_destino}}`

- Gera uma arquivo com um número específico de bytes aleatórios, usando o dispositivo aleatório do kernel:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{caminho/para/arquivo_aleatorio}}`

- Cria um benchmark do desempenho de escrita de um disco:

`dd bs={{1M}} count={{1024}} if=/dev/zero of={{caminho/para/arquivo_1GB}}`

- Cria uma cópia de segurança do sistema, salva em um arquivo IMG (pode ser restaurado depois trocando o valor de `if` com o de `of`), e mostra o progresso:

`dd if={{/dev/dispositivo_de_origem}} of={{caminho/para/arquivo.img}} status=progress`

- Verifica o progresso de uma operação `dd` que está acontecendo (execute esse comando em outro terminal):

`kill -USR1 $(pgrep -x dd)`
