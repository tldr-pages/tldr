# dpkg-query

> Mostra informações dos pacotes instalados.
> Mais informações: <https://manned.org/dpkg-query.1>.

- Exibe todos os pacotes instalados:

`dpkg-query --list`

- Exibe os pacotes instalados correspondentes ao critério de busca:

`dpkg-query --list '{{libc6}}'`

- Exibe todos os arquivos instalados por um pacote:

`dpkg-query --listfiles {{libc6}}`

- Exibe informações sobre um pacote:

`dpkg-query --status {{libc6}}`

- Busca por pacotes que contenham arquivos que correspondam ao padrão:

`dpkg-query --search {{/etc/ld.so.conf.d}}`
