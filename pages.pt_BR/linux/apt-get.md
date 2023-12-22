# apt-get

> Gerenciador de pacotes das distribuições baseadas em Debian.
> Procure por pacotes utilizando o `apt-cache`.
> Mais informações: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Atualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt-get`):

`apt-get update`

- Instala um pacote ou atualizá-lo para a versão mais recente:

`apt-get install {{nome_do_pacote}}`

- Remove um pacote:

`apt-get remove {{nome_do_pacote}}`

- Remove um pacote e os seus arquivos de configuração:

`apt-get purge {{nome_do_pacote}}`

- Atualiza todos os pacotes instalados para as versões mais recentes:

`apt-get upgrade`

- Limpa o repositório local — removendo os arquivos de pacotes (`.deb`) de downloads interrompidos que não podem mais ser baixados:

`apt-get autoclean`

- Remove todos os pacotes obsoletos:

`apt-get autoremove`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`apt-get dist-upgrade`
