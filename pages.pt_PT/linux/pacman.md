# pacman

> Utilitário para gerir pacotes Arch Linux.
> Veja também: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincroniza e actualiza todos os pacotes:

`sudo pacman -Syu`

- Instala um novo pacote:

`sudo pacman -S {{package_name}}`

- Remove um pacote e todas as dependencias:

`sudo pacman -Rs {{nome_do_pacote}}`

- Procura um pacote na base de dados por palavra chave ou expressão regular (regex):

`pacman -Ss "{{search_pattern}}"`

- Lista versão dos pactotes instalados:

`pacman -Q`

- Lista versão dos pactotes instalados explicitamente:

`pacman -Qe`

- Lista pacotes órfãos (instalados como dependencia mas não exigidos por nenhum pacote):

`pacman -Qtdq`

- Remove memória armazenada (cache) do `pacman`:

`sudo pacman -Scc`
