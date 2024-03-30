# xrandr

> Define o tamanho, orientação e/ou espelhamento das saídas para uma tela.
> Mais informações: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Exibe o estado atual do sistema (telas conhecidas, resoluções, ...):

`xrandr --query`

- Desativa saídas desconectadas e ativa as conectadas com as configurações padrão:

`xrandr --auto`

- Altera a resolução e frequência de atualização da DisplayPort 1 para 1920x1080, 60Hz:

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- Define a resolução do HDMI2 para 1280x1024 e o coloca à direita de DP1:

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- Desativa a saída VGA1:

`xrandr --output {{VGA1}} --off`

- Define o brilho de LVDS1 como 50%:

`xrandr --output {{LVDS1}} --brightness {{0.5}}`
