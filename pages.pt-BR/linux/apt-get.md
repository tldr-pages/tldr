# apt-get

> Utilitário de gerenciamento de pacotes para distribuições Debian e Ubuntu.
> Procure por pacotes utilizando o `apt-cache`.

- Atualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt-get`):

`apt-get update`

- Instala um pacote ou o atualiza para a versão mais recente:

`apt-get install {{package}}`

- Remove um pacote:

`apt-get remove {{package}}`

- Remove um pacote e os seus arquivos de configuração:

`apt-get purge {{package}}`

- Atualiza todos os pacotes instalados para as versões mais recentes:

`apt-get upgrade`

- Remove todos os pacotes obsoletos:

`apt-get autoremove`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém remove os pacotes obsoletos e instala pacotes adicionais necessários por novas dependências:

`apt-get dist-upgrade`
