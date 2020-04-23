# dpkg-query

> Ferramenta que mostra informações dos pacotes instalados.

- Exibir os pacotes instalados:

`dpkg-query -l`

- Exibir os pacotes instalados correspondentes ao critério de busca:

`dpkg-query -l '{{criterio_de_busca}}'`

- Exibir todos os arquivos instalados por um pacote:

`dpkg-query -L {{nome_do_pacote}}`

- Exibir informações sobre um pacote:

`dpkg-query -s {{nome_do_pacote}}`
