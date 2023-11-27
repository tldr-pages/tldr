# dd

> Converte e copia um arquivo.
> Mais informações: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Cria uma unidade USB inicializável a partir de um arquivo isohybrid (tal como `archlinux-xxx.iso`):

`dd if={{arquivo.iso}} of=/dev/{{unidade_usb}}`

- Clona uma unidade para outra unidade com bloco de 4 MB e ignora erro:

`dd if=/dev/{{unidade_origem}} of=/dev/{{unidade_destino}} bs=4m conv=noerror`

- Gera um arquivo de 100 bytes aleatórios usando o driver aleatório do kernel:

`dd if=/dev/urandom of={{arquivo_aleatório}} bs=100 count=1`

- Compara o desempenho de gravação de um disco:

`dd if=/dev/zero of={{arquivo_1GB}} bs=1024 count=1000000`
