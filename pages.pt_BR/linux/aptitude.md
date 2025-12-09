# aptitude

> Utilitário de gerenciamento de pacotes de Debian e Ubuntu.
> Mais informações: <https://manned.org/aptitude.8>.

- Sincroniza a lista de pacotes e versões disponíveis. Deve ser executado antes de outros comandos `aptitude`:

`aptitude update`

- Instala um novo pacote e suas dependências:

`aptitude install {{pacote}}`

- Busca por um determinado pacote:

`aptitude search {{pacote}}`

- Busca por uma determinado pacote instalado (`?installed` é um termo de busca `aptitude`):

`aptitude search '?installed({{pacote}})'`

- Remove um pacote e todos que dependam dele:

`aptitude remove {{pacote}}`

- Atualiza os pacotes instalados para suas versões mais recentes:

`aptitude upgrade`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`aptitude full-upgrade`

- Coloca um pacote instalado em espera para prevenir atualizações automáticas:

`aptitude hold '?installed({{pacote}})'`
