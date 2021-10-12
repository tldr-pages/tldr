# ftp

> Ferramentas para interagir com um servidor via Protocolo de Transferência de Arquivos.
> Mais informações: <https://manned.org/ftp>.

- Conecta-se a um servidor FTP:

`ftp {{ftp.exemplo.com}}`

- Alterna para o modo de transferência binária (gráficos, arquivos compactados, etc):

`binary`

- Transfere vários arquivos sem solicitar confirmação em cada arquivo:

`prompt off`

- Baixa vários arquivos (expressão glob):

`mget {{*.png}}`

- Carrega vários arquivos (expressão glob):

`mput {{*.zip}}`

- Exclui vários arquivos no servidor remoto:

`mdelete {{*.txt}}`

- Renomeia um arquivo no servidor remoto:

`rename {{nome_do_arquivo_original}} {{nome_do_novo_arquivo}}`
