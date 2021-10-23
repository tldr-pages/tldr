# apt

> Gestor de pacotes das distribuições baseadas em Debian.
> Mais informações: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Actualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt`):

`sudo apt update`

- Pesquisa pacotes correspondentes ao critério de pesquisa:

`apt search {{criterio_de_pesquisa}}`

- Exibe as informações de um pacote:

`apt show {{nome_do_pacote}}`

- Instala um pacote ou actualiza-o para a versão mais recente:

`sudo apt install {{nome_do_pacote}}`

- Remove um pacote (Para remover os ficheiros de configuração deve-se usar a opção `purge` em vez de `remove`):

`sudo apt remove {{nome_do_pacote}}`

- Actualiza os pacotes instalados para as versões mais recentes:

`sudo apt upgrade`
