# vimdiff

> Deschideți două sau mai multe fișiere în vim și afișați diferențele dintre ele.
> A se vedea, de asemenea, `vim`.
> Mai multe informaţii: <https://www.vim.org>

- Deschideți două fișiere și arătați diferențele:

`vimdiff {{file1}} {{file2}}`

- Mutați cursorul în fereastra din stânga|dreapta:

`Ctrl + w {{h|l}}`

- Salt la următoarea diferență:

`[c`

- Salt la diferența anterioară:

`]c`

- Copiați diferența evidențiată din cealaltă fereastră în fereastra curentă:

`do`

- Copiați diferența evidențiată din fereastra curentă în cealaltă fereastră:

`dp`

- Actualizați toate evidențele și pliurile:

`:diffupdate`

- Comută plierea codului evidențiat:

`za`
