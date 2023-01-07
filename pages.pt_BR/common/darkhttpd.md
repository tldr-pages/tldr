# darkhttpd

> Servidor web Darkhttpd.
> Mais informações: <https://unix4lyfe.org/darkhttpd>.

- Inicia o servidor servindo a raiz do documento especificada:

`darkhttpd {{caminho/para/raiz_do_documento}}`

- Inicia o servidor na porta especificada (porta 8080 por padrão se estiver executando como usuário não raiz):

`darkhttpd {{caminho/para/raiz_do_documento}} --port {{porta}}`

- Escuta apenas no endereço IP especificado (por padrão, o servidor escuta em todas as interfaces):

`darkhttpd {{caminho/para/raiz_do_documento}} --addr {{endereço_de_ip}}`
