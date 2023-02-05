# nvim

> A Neovim, egy Vim alapú programozói szövegszerkesztő, többféle üzemmódot biztosít a különböző szövegmanipulációkhoz.
> A `i` megnyomásával normál módban a beszúrási módba léphetünk. `<Esc>` visszatér a normál módba, amely nem teszi lehetővé a normál szöveg beszúrását.
> Lásd még: `vim`, `vimtutor`, `vimdiff`.
> További információ: <https://neovim.io>.

- Fájl megnyitása:

`nvim {{path/to/file}}`

- Szövegszerkesztési módba (beszúrási mód) való belépés:

`<Esc>i`

- Másolja ("yank") vagy vágja ki ("delete") az aktuális sort (beillesztés a `P` segítségével):

`<Esc>{{yy|dd}}`

- Lépjen normál üzemmódba, és vonja vissza az előző műveletet:

`<Esc>u`

- Mintakeresés a fájlban (a `n`/`N` gomb megnyomásával a következő/előző találatra léphet):

`<Esc>/{{search_pattern}}<Enter>`

- Szabályos kifejezés helyettesítés végrehajtása az egész fájlban:

`<Esc>:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- Normál üzemmódba lépés és a fájl mentése (írása), majd kilépés:

`<Esc>:wq<Enter>`

- Kilépés mentés nélkül:

`<Esc>:q!<Enter>`
