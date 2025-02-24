# makepkg

> Monta um pacote que pode ser usado junto ao `pacman`.
> Utiliza por padrão o arquivo `PKGBUILD` no diretório de trabalho atual.
> Mais informações: <https://manned.org/makepkg.8>.

- Monta um pacote:

`makepkg`

- Monta um pacote e instala suas dependências:

`makepkg {{[-s|--syncdeps]}}`

- Monta um pacote, instala suas dependências e então o instala no sistema:

`makepkg {{[-s|--syncdeps]}} {{[-i|--install]}}`

- Monta um pacote, mas pula a verificação de hashes da fonte:

`makepkg --skipchecksums`

- Limpa os diretórios de trabalho após uma compilação bem sucedida:

`makepkg {{[-c|--clean]}}`

- Verifica os hashes das fontes:

`makepkg --verifysource`

- Gera e salva as informações da fonte no arquivo `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
