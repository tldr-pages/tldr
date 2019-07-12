# axel

> Acelerador de downloads.
> Suporta HTTP, HTTPS, e FTP.
> Página oficial: <https://github.com/axel-download-accelerator/axel>.

- Fazer download de uma URL para um arquivo:

`axel {{url}}`

- Fazer download especificando o nome do arquivo de destino:

`axel {{url}} -o {{nome_do_arquivo}}`

- Fazer download usando múltiplas conexões:

`axel -n {{numero_de_conexoes}} {{url}}`

- Procurar por mirrors:

`axel -S {{numero_de_mirrors}} {{url}}`

- Limitar velocidade de download (em bytes por segundo):

`axel -s {{velocidade}} {{url}}`
