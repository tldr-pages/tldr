# i3lock

> Bloqueador de tela simples para o i3wm.
> Mais informações: <https://i3wm.org/i3lock>.

- Bloqueia a tela com uma cor de fundo (formato rrggbb):

`i3lock -c {{0000ff}}`

- Bloqueia a tela com uma imagem PNG:

`i3lock -i {{local/da/imagem.png}}`

- Desabilita o indicador de desbloqueio (remove a resposta ao apertar teclas):

`i3lock -u`

- Exibe o ponteiro do mouse ao invés de ocultá-lo ('default' para o ponteiro padrão, 'win' para um ponteiro MS Windows):

`i3lock -p {{default|win}}`

- Bloqueia a tela com uma imagem PNG exibida em múltiplos monitores, com o ponteiro do mouse habilitado:

`i3lock -i {{local/da/imagem.png}} -p {{default|win}} -t`
