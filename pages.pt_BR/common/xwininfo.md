# xwininfo

> Mostra informações sobre janelas.
> Veja também: `xprop`, `xkill`.
> Mais informações: <https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>.

- Mostra um cursor para selecionar uma janela para mostrar seus atributos (ID, nome, tamanho, posição...):

`xwininfo`

- Mostra a árvore de todas as janelas:

`xwininfo -tree -root`

- Mostra os atributos de uma janela com um ID específico:

`xwininfo -id {{id}}`

- Mostra os atributos de uma janela com um nome específico:

`xwininfo -name {{nome}}`

- Mostra o ID de uma janela buscando pelo nome:

`xwininfo -tree -root | grep {{palavra_chave}} | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
