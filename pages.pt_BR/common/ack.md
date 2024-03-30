# ack

> Uma ferramenta de pesquisa similar ao grep, otimizada para programadores.
> Mais informações: <https://beyondgrep.com/documentation>.

- Procura por arquivos que contenham o termo "foo":

`ack {{foo}}`

- Procura por arquivos em uma linguagem específica:

`ack --ruby {{each_with_object}}`

- Conta o número total de correspondências para o termo "foo":

`ack -ch {{foo}}`

- Mostra o nome dos arquivos contendo o termo "foo" e o número de correspondências em cada arquivo:

`ack -cl {{foo}}`
