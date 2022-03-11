# pacman

> Utilitário de Arch Linux para gerenciamento de pacotes.
> Alguns subcomandos como `pacman sync` possuem sua própria documentação de uso.
> Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincroniza e atualiza todos os pacotes:

`sudo pacman --sync --refresh --sysupgrade`

- Instala um novo pacote:

`sudo pacman --sync {{nome_do_pacote}}`

- Remove um pacote e suas dependências:

`sudo pacman --remove --recursive {{nome_do_pacote}}`

- Procura no banco de dados de pacotes por uma expressão regular ou palavra-chave:

`pacman --sync --search "{{padrao_buscado}}"`

- Lista pacotes instalados e versões:

`pacman --query`

- Lista apenas os pacotes explicitamente instalados e versões:

`pacman --query --explicit`

- Lista pacotes órfãos (instalado como dependência mas não requerido por qualquer pacote):

`pacman --query --unrequired --deps --quiet`

- Esvazia completamente o cache do pacman:

`sudo pacman --sync --clean --clean`
