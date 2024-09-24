# bspc

> Configura e controla `bspwm`, gerenciando nós, áreas de trabalho, monitores, e outros.
> Veja também: `bspwm`.
> Mais informações: <https://github.com/baskerville/bspwm>.

- Define duas áreas de trabalho virtuais:

`bspc monitor --reset-desktops {{nome_da_area_1}} {{nome_da_area_2}}`

- Foca em uma área de trabalho determinada:

`bspc desktop --focus {{numero}}`

- Fecha as janelas atreladas ao nó selecionado:

`bspc node --close`

- Envia o nó selecionado para uma área de trabalho determinada:

`bspc node --to-desktop {{numero}}`

- Alterna o nó selecionado para modo de tela cheia:

`bspc node --state ~fullscreen`

- Define o valor de uma configuração específica:

`bspc config {{nome_da_configuracao}} {{valor}}`
