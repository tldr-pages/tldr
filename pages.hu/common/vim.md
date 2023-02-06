# vim

> A Vim (Vi IMproved), egy parancssori szövegszerkesztő, többféle üzemmódot biztosít a különböző szövegmanipulációkhoz.
> A `i` megnyomásával normál üzemmódban a beszúrási üzemmódba léphetünk.
> A `<Esc>` megnyomásával visszatér a normál módba, amely lehetővé teszi a Vim-parancsok használatát.
> Lásd még: `vimdiff`, `vimtutor`, `nvim`.
> További információ: <https://www.vim.org>.

- Fájl megnyitása:

`vim {{path/to/file}}`

- Egy fájl megnyitása egy megadott sorszámnál:

`vim +{{line_number}} {{path/to/file}}`

- A Vim súgó kézikönyvének megtekintése:

`:help<Enter>`

- Az aktuális puffer mentése és kilépése:

`:wq<Enter>`

- Normál üzemmódba lépés és az utolsó művelet visszavonása:

`<ESC>u`

- Mintakeresés a fájlban (a `n`/`N` gomb megnyomásával a következő/előző találatra léphet):

`/{{search_pattern}}<Enter>`

- Szabályos kifejezés helyettesítése a teljes fájlban:

`:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- A sorszámok megjelenítése:

`:set nu<Enter>`
