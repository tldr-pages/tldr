# zathura

> Um visualizador de documentos modular e baseado em vim, com uma linha de comando integrada.
> Tenha certeza de que um backend está instalado (poppler, PostScript, ou DjVu).
> Mais informações: <https://pwmt.org/projects/zathura/>.

- Abre um arquivo:

`zathura {{caminho/para/arquivo}}`

- Navega esquerda/baixo/cima/direita:

`{{<h>|<j>|<k>|<l>|<ArrowKeys>}}`

- Rotaciona:

`<r>`

- Inverte cores:

`<Ctrl r>`

- Procura por uma string no documento:

`</>{{string}}`

- Cria/remove marcadores de página:

`<:>{{bmark|bdelete}} {{nome_do_marcador}}<Enter>`

- Lista marcadores de página:

`<:>blist<Enter>`
