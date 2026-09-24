# pacman --files

> Utilitário de Arch Linux para gerenciamento de pacotes.
> Veja também: `pacman`, `pkgfile`.
> Mais informações: <https://manned.org/pacman.8>.

- Atualiza o banco de dados de pacotes:

`sudo pacman -Fy`

- Procura o pacote que possui um arquivo específico:

`pacman -F {{nome_arquivo}}`

- Encontra o pacote que possui um arquivo específico, usando uma expressão regular:

`pacman -Fx '{{expressao_regular}}'`

- Lista apenas os nomes de pacotes:

`pacman -Fq {{nome_arquivo}}`

- Lista os arquivos de um pacote específico:

`pacman -Fl {{pacote}}`

- Exibe ajuda:

`pacman -Fh`
