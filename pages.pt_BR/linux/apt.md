# apt

> Utilitário de gerenciamento de pacotes de distribuições baseadas em Debian.
> Substituto recomendado para `apt-get` quando usado de forma interativa em versões do Ubuntu mais novas que 16.04.
> Para comandos equivalentes em outros gerenciadores de pacotes, veja <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Mais informações: <https://manned.org/apt.8>.

- Atualiza a lista de pacotes e versões disponíveis (recomenda-se executá-lo antes de outros comandos `apt`):

`sudo apt update`

- Busca por um determinado pacote:

`apt search {{pacote}}`

- Exibe as informações de um pacote:

`apt show {{pacote}}`

- Instala um pacote ou atualiza-o para a versão mais recente:

`sudo apt install {{pacote}}`

- Remove um pacote (para remover também os arquivos de configuração deve-se usar a opção `purge` ao invés do `remove`):

`sudo apt remove {{pacote}}`

- Atualiza todos os pacotes instalados para suas versões mais recentes:

`sudo apt upgrade`

- Lista todos os pacotes:

`apt list`

- Lista todos os pacotes instalados:

`apt list {{[-i|--installed]}}`
