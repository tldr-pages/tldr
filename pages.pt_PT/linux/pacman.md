# pacman

> Utilitário para gerir pacotes Arch Linux.
> Veja também: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`,  `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincronizar e actualizar todos os pacotes:

`sudo pacman -Syu`

- Instalar um novo pacote:

`sudo pacman -S {{package_name}}`

- Remover um pacote e todas as dependencias:

`sudo pacman -Rs {{nome_do_pacote}}`

- Procurar um pacote na base de dados por palavra chave ou expressão regular (regex):

`pacman -Ss "{{search_pattern}}"`

- Listar versão dos pactotes instalados:

`pacman -Q`

- Listar versão dos pactotes instalados explicitamente:

`pacman -Qe`

- Listar pacotes órfãos (instalados como dependencia mas não exigidos por nenhum pacote):

`pacman -Qtdq`

- Remover memória armazenada (cache) do `pacman`:

`sudo pacman -Scc`
