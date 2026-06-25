# i3lock

> Bloqueador de tela simples para o gerenciador de janelas i3.
> Mais informações: <https://manned.org/i3lock>.

- Bloqueia a tela com uma tela branca:

`i3lock`

- Bloqueia a tela com uma cor de fundo (formato rrggbb):

`i3lock {{[-c|--color]}} {{0000ff}}`

- Bloqueia a tela com uma imagem PNG:

`i3lock {{[-i|--image]}} {{caminho/para/imagem.png}}`

- Bloqueia a tela e disabilita o indicador de desbloqueio (remove as resposta do sistema ao pressionar alguma tecla):

`i3lock {{[-u|--no-unlock-indicator]}}`

- Bloqueia a tela e não esconde o ponteiro do mouse:

`i3lock {{[-p|--pointer]}} {{default}}`

- Bloqueia a tela com uma imagem PNG sendo mostrada em todos os monitores:

`i3lock {{[-i|--image]}} {{path/to/imagem.png}} {{[-t|--tiling]}}`

- Bloqueia a tela e mostra o número de tentativas de login que falharam:

`i3lock {{[-f|--show-failed-attempts]}}`
