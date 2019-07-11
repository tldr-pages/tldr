# axel

> Acelerador de downloads.
> Suporta HTTP, HTTPS, e FTP.
> Página Oficial: <https://github.com/axel-download-accelerator/axel>.

- Fazer download de uma URL para um arquivo:

`axel {{url}}`

- Fazer download especificando o nome do arquivo destino:

`axel {{url}} -o {{nome_do_arquivo}}`

- Fazer download usando multiplas conexões:

`axel -n {{numero_de_conexoes}} {{url}}`

- Procurar por mirrors:

`axel -S {{numero_de_mirrors}} {{url}}`

- Limitar velocidade de download (bytes por segundo):

`axel -s {{velocidade}} {{url}}`
