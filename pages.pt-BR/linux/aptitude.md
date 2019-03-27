# aptitude

> Utilitário de gerenciamento de pacotes das distribuições baseadas em Debian.

- Sincroniza a lista de pacotes e versões disponíveis. Deve ser executado antes de comandos aptitude subsequentes:

`aptitude update`

- Instala um novo pacote e suas dependências:

`aptitude install {{package}}`

- Busca por pacotes que atendam o critério de busca:

`aptitude search {{package}}`

- Remove um pacote e todos que dependam dele:

`aptitude remove {{package}}`

- Atualiza todos os pacotes instalados para as versões mais recentes:

`aptitude upgrade`

- UAtualiza os pacotes instalados (semelhante ao `aptitude upgrade`), porém remove os pacotes obsoletos e instala pacotes adicionais necessários por novas dependências:

`aptitude full-upgrade`
