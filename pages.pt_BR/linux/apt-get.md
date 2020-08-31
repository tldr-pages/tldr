# apt-get

> Gerenciador de pacotes das distribuições baseadas em Debian.
> Procure por pacotes utilizando o `apt-cache`.

- Atualizar a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt-get`):

`apt-get update`

- Instalar um pacote ou atualizá-lo para a versão mais recente:

`apt-get install {{nome_do_pacote}}`

- Remover um pacote:

`apt-get remove {{nome_do_pacote}}`

- Remover um pacote e os seus arquivos de configuração:

`apt-get purge {{nome_do_pacote}}`

- Atualizar todos os pacotes instalados para as versões mais recentes:

`apt-get upgrade`

-  Limpar o repositório local — removendo os arquivos de pacotes (.deb) de downloads interrompidos que não podem mais ser baixados:

`apt-get autoclean`

- Remover todos os pacotes obsoletos:

`apt-get autoremove`

- Atualizar os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`apt-get dist-upgrade`
