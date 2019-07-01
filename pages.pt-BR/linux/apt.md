# apt

> Gerenciador de pacotes das distribuições baseadas em Debian.

- Atualizar a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt`):

`sudo apt update`

- Buscar pacotes correspondentes ao critério de busca:

`apt search {{criterio_de_busca}}`

- Exibir as informações de pacote:

`apt show {{nome_do_pacote}}`

- Instalar um pacote ou atualizá-lo para a versão mais recente:

`sudo apt install {{nome_do_pacote}}`

- Remover um pacote (Para remover os arquivos de configuração deve-se usar a opção `purge` ao invés do `remove`):

`sudo apt remove {{nome_do_pacote}}`

- Atualizar os pacotes instalados para as versões mais recentes:

`sudo apt upgrade`
