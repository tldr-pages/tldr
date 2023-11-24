# vimdiff

> Open twee of meer bestanden in `vim` en toon de verschillen tussen ze.
> Bekijk ook: `vim`, `vimtutor`, `nvim`.
> Meer informatie: <https://www.vim.org>.

- Open twee bestanden en toon de verschillen:

`vimdiff {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Verplaats de cursor naar het scherm links|rechts:

`Ctrl + w {{h|l}}`

- Spring naar het vorige verschil:

`[c`

- Spring naar het volgende verschil:

`]c`

- Copy the highlighted difference from the other window to the current window:

`do`

- Copy the highlighted difference from the current window to the other window:

`dp`

- Update alle markeringen en folds:

`:diffupdate`

- Schakel de gemarkeerde code fold om:

`za`
