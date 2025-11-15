# vimdiff

> Open twee of meer bestanden in `vim` en toon de verschillen.
> Zie ook: `vim`, `vimtutor`, `nvim`.
> Meer informatie: <https://www.vim.org>.

- Open twee bestanden en toon de verschillen:

`vimdiff {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Verplaats de cursor naar het scherm links|rechts:

`<Ctrl w>{{<h>|<l>}}`

- Spring naar het vorige verschil:

`<[><c>`

- Spring naar het volgende verschil:

`<]><c>`

- Kopieer het gemarkeerde verschil van het andere scherm naar het huidige scherm:

`<d><o>`

- Kopieer het gemarkeerde verschil van het huidige scherm naar het andere scherm:

`<d><p>`

- Update alle markeringen en folds:

`<:>diffupdate`

- Schakel de gemarkeerde code fold om:

`<z><a>`
