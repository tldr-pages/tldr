# apt

> Utilitário de gerenciamento de pacotes das distribuições baseadas em Debian.

- Atualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt`)::

`sudo apt update`

- Busca por pacotes que atendam o critério de busca:

`apt search {{package}}`

- Exibe as informações de um determinado pacote:

`apt show {{package}}`

- Instala um pacote ou o atualiza para a versão mais recente:

`sudo apt install {{package}}`

- Remove um pacote (Para remove os arquivos de configuração então deve-se usar a opção `purge` ao invés do `remove`):

`sudo apt remove {{package}}`

- Atualiza todos os pacotes instalados para as versões mais recentes:

`sudo apt upgrade`
