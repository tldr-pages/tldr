# aptitude

> Gerenciador de pacotes das distribuições baseadas em Debian.
> Mais informações: <https://manned.org/aptitude.8>.

- Atualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `aptitude`):

`aptitude update`

- Instala um novo pacote e suas dependências:

`aptitude install {{nome_do_pacote}}`

- Busca pacotes correspondentes ao critério de busca:

`aptitude search {{criterio_de_busca}}`

- Remove um pacote e todos que dependam dele:

`aptitude remove {{nome_do_pacote}}`

- Atualiza os pacotes instalados para as versões mais recentes:

`aptitude upgrade`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`aptitude full-upgrade`
