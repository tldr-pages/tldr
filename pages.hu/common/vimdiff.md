# vimdiff

> Nyisson meg két vagy több fájlt a vimben, és mutassa meg a köztük lévő különbségeket. Lásd még: `vim`, `vimtutor`, `nvim`. További információ: <https://www.vim.org>.

- Nyisson meg két fájlt, és mutassa meg a különbségeket:

`vimdiff {{file1}} {{file2}}`

- Mozgassa a kurzort a bal|jobb oldali ablakra:

`Ctrl + w {{h|l}}`

- Ugrás az előző különbségre:

`[c`

- Ugrás a következő különbségre:

`]c`

- A kiemelt különbség másolása a másik ablakból az aktuális ablakba:

`do`

- A kiemelt különbség másolása az aktuális ablakból a másik ablakba:

`dp`

- Az összes kiemelt és hajtogatott különbség frissítése:

`:diffupdate`

- A kiemelt kód hajtogatásának váltása:

`za`
