# nvim

> Neovim, un editor di testo basato su Vim che offre molti diversi modi di manipolare e navigare il testo.
> Premere `i` per entrare in modalità inserimento (insert mode), `<Esc>` per uscire e tornare alla modalità normale (normal mode).
> Maggiori informazioni: <https://neovim.io>.

- Aprire un file:

`nvim {{file}}`

- Entrare nella modalità per scrivere testo (insert mode):

`<Esc>i`

- Copiare ("yank") o cancellare ("delete") la linea corrente (può poi essere copiata con `p` o `P`):

`<Esc>{{yy|dd}}`

- Annullare l'ultima operazione fatta:

`<Esc>u`

- Cercare uno specifico pattern nel file (premere `n`/`N` per navigare tra le occorrenze successive/precedenti):

`<Esc>/{{patter_da_cercare}}<Enter>`

- Eseguire una sostituzione tramite espressione regolare nell'intero file:

`<Esc>:%s/{{espressione_regolare}}/{{sostituzione}}/g<Enter>`

- Salvare (scrivere) il file per poi uscire:

`<Esc>:wq<Enter>`

- Uscire senza salvare:

`<Esc>:q!<Enter>`
