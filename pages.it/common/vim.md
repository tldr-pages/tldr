# vim

> Vi IMproved, un editor di testo per programmatori che fornisce diverse modalità per modificare testo.
> Premi `i` per entrare in insert mode e `<Esc>` per tornare in normal mode dove non puoi inserire testo normalmente.
> Maggiori informazioni: <https://www.vim.org>.

- Apri un file in vim:

`vim {{file}}`

- Annulla l'ultima operazione:

`<Esc>u`

- Cerca un pattern nel file (usa `n`/`N` per spostarti al risultato successivo/precedente):

`/{{espressione_regolare}}<Invio>`

- Effettua una sostituzione tramite espressione regolare nell'intero file:

`:%s/{{espressione_regolare}}/{{sostituzione}}/g<Invio>`
