# pacman

> Utilitário para gerir pacotes Arch Linux.
> Sub comandos como `pacman sync` tem a sua própria documentação.
> Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincronizar e actualizar todos os pacotes:

`sudo pacman --sync --refresh --sysupgrade`

- Instalar um novo pacote:

`sudo pacman --sync {{package_name}}`

- Remover um pacote e todas as dependencias:

`sudo pacman --remove --recursive {{nome_do_pacote}}`

- Procurar um pacote na base de dados por palavra chave ou expressão regular (regex):

`pacman --sync --search "{{search_pattern}}"`

- Listar versão dos pactotes instalados:

`pacman --query`

- Listar versão dos pactotes instalados explicitamente:

`pacman --query --explicit`

- Listar pacotes órfãos (instalados como dependencia mas não exigidos por nenhum pacote):

`pacman --query --unrequired --deps --quiet`

- Remover memória armazenada (cache) do `pacman`:

`sudo pacman --sync --clean --clean`
