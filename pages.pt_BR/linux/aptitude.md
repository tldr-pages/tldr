# aptitude

> Gerenciador de pacotes das distribuições baseadas em Debian.

- Atualizar a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `aptitude`):

`aptitude update`

- Instalar um novo pacote e suas dependências:

`aptitude install {{nome_do_pacote}}`

- Buscar pacotes correspondentes ao critério de busca:

`aptitude search {{criterio_de_busca}}`

- Remover um pacote e todos que dependam dele:

`aptitude remove {{nome_do_pacote}}`

- Atualizar os pacotes instalados para as versões mais recentes:

`aptitude upgrade`

- Atualizar os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`aptitude full-upgrade`
