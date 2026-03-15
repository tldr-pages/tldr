# dpkg-query

> Mostra informações dos pacotes instalados.
> Mais informações: <https://manned.org/dpkg-query>.

- Exibe todos os pacotes instalados:

`dpkg-query {{[-l|--list]}}`

- Exibe os pacotes instalados correspondentes ao critério de busca:

`dpkg-query {{[-l|--list]}} '{{libc6*}}'`

- Exibe todos os arquivos instalados por um pacote:

`dpkg-query {{[-L|--listfiles]}} {{libc6}}`

- Exibe informações sobre um pacote:

`dpkg-query {{[-s|--status]}} {{libc6}}`

- Busca por pacotes que contenham arquivos que correspondam ao padrão:

`dpkg-query {{[-S|--search]}} {{/etc/ld.so.conf.d}}`
