# vim

> Vi IMproved, un editor di testo per programmatori che fornisce diverse modalità per modificare testo.
> Premi `i` per entrare in insert mode e `<Esc>` per tornare in normal mode dove non puoi inserire testo normalmente.
> Maggiori informazioni: <https://www.vim.org>.

- Apri un file in vim:

`vim {{file}}`

- Vai in insert mode (per inserire testo):

`<Esc>i`

- Copia ("yank") o taglia ("delete") la linea corrente (per incollarla poi con `P`):

`<Esc>{{yy|dd}}`

- Annulla l'ultima operazione:

`<Esc>u`

- Cerca un pattern nel file (usa `n`/`N` per spostarti al risultato successivo/precedente):

`<Esc>/{{pattern}}<Invio>`

- Effettua una sostituzione tramite regex nell'intero file:

`<Esc>:%s/{{pattern}}/{{sostituzione}}/g<Invio>`

- Salva modifiche al file ed esci:

`<Esc>:wq<Invio>`

- Esci senza salvare:

`<Esc>:q!<Invio>`
