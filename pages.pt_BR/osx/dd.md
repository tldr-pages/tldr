# dd

> Converte e copia um arquivo.
> Mais informações: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Cria uma unidade USB inicializável a partir de um arquivo isohybrid (tal como `archlinux-xxx.iso`) e mostra o progresso:

`dd if={{caminho/para/arquivo.iso}} of={{/dev/unidade_usb}} status=progress`

- Clona uma unidade para outra unidade com bloco de 4 MB, ignora qualquer erro e mostra o progresso:

`dd bs=4m conv=noerror if={{/dev/unidade_origem}} of={{/dev/unidade_destino}} status=progress`

- Gera um arquivo de número específico de bytes aleatórios usando o driver aleatório do kernel:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{caminho/para/arquivo_aleatório}}`

- Compara o desempenho de gravação de um disco:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{caminho/para/arquivo_1GB}}`

- Cria um backup do sistema, salva-o em um arquivo IMG (pode ser restaurado posteriormente permutando `if` e `of`) e mostra o progresso:

`dd if={{/dev/dispositivo_unidade}} of={{caminho/para/arquivo.img}} status=progress`

- Verifica o progresso de uma operação `dd` em andamento (execute este comando de outro shell):

`kill -USR1 $(pgrep ^dd)`
