# apt

> Gestor de pacotes das distribuições baseadas em Debian.
> Mais informações: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Actualizar a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt`):

`sudo apt update`

- Pesquisa pacotes correspondentes ao critério de pesquisa:

`apt search {{criterio_de_pesquisa}}`

- Exibir as informações de um pacote:

`apt show {{nome_do_pacote}}`

- Instalar um pacote ou actualizá-lo para a versão mais recente:

`sudo apt install {{nome_do_pacote}}`

- Remover um pacote (Para remover os ficheiros de configuração deve-se usar a opção `purge` em vez de `remove`):

`sudo apt remove {{nome_do_pacote}}`

- Actualizar os pacotes instalados para as versões mais recentes:

`sudo apt upgrade`
