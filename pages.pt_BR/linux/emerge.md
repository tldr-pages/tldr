# emerge

> Utilitário de gerenciamento de pacotes do Gentoo Linux.
> Para comandos equivalentes em outros gerenciadores de pacotes, veja <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Mais informações: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Sincronizar todos os pacotes:

`sudo emerge --sync`

- Atualiza todos os pacotes, incluindo dependências:

`sudo emerge {{[-avuDN|--ask --verbose --update --deep --newuse]}} @world`

- Resume uma atualização falha, pulando o pacote que falhou:

`sudo emerge --resume --skipfirst`

- Instala um novo pacote, com confirmação:

`sudo emerge {{[-av|--ask --verbose]}} {{pacote}}`

- Remove um pacote e suas dependências com confirmação:

`sudo emerge {{[-avc|--ask --verbose --depclean]}} {{pacote}}`

- Remove pacotes órfãos (instalados como dependências mas não são mais requisitados por nenhum pacote):

`sudo emerge {{[-avc|--ask --verbose --depclean]}}`

- Procura na base de dados por uma palavra-chave:

`emerge {{[-S|--searchdesc]}} {{palavra-chave}}`
