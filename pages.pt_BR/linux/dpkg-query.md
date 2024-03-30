# dpkg-query

> Ferramenta que mostra informações dos pacotes instalados.
> Mais informações: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

- Exibe os pacotes instalados:

`dpkg-query -l`

- Exibe os pacotes instalados correspondentes ao critério de busca:

`dpkg-query -l '{{criterio_de_busca}}'`

- Exibe todos os arquivos instalados por um pacote:

`dpkg-query -L {{nome_do_pacote}}`

- Exibe informações sobre um pacote:

`dpkg-query -s {{nome_do_pacote}}`
