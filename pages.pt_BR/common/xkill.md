# xkill

> Termina uma janela interativamente em uma sessão gráfica.
> Veja também: `kill`, `killall`.
> Mais informações: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- Ativa um cursor para fechar uma janela com o clique do botão esquerdo do mouse (pressionar qualquer outro botão para cancelar):

`xkill`

- Mostra um cursor para selecionar uma janela pressionando qualquer botão do mouse:

`xkill -button any`

- Fecha uma janela com um ID específico (use `xwininfo` para obter informações sobre janelas):

`xkill -id {{id}}`
