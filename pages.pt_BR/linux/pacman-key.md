# pacman-key

> Script envoltório para o GnuPG usado para gerenciar o chaveiro do pacman.
> Veja também: `pacman`.
> Mais informações: <https://manned.org/pacman-key>.

- Inicializa o chaveiro do `pacman`:

`sudo pacman-key --init`

- Adiciona as chaves padrão do Arch Linux:

`sudo pacman-key --populate {{archlinux}}`

- Lista chaves do chaveiro público:

`pacman-key --list-keys`

- Adiciona as chaves especificadas:

`sudo pacman-key --add {{caminho/para/arquivo_chave.gpg}}`

- Recebe uma chave do servidor de chaves:

`sudo pacman-key --recv-keys "{{uid|nome|email}}"`

- Imprime a impressão digital de uma chave específica:

`pacman-key --finger "{{uid|nome|email}}"`

- Assina uma chave importada localmente:

`sudo pacman-key --lsign-key "{{uid|nome|email}}"`

- Remove uma chave específica:

`sudo pacman-key --delete "{{uid|nome|email}}"`
