# ipaggmanip

> A `ipaggcreate` által készített összesített statisztikák kezelése. További információ: <https://manned.org/ipaggmanip>.

- Kombinálja a magasrendű bitjeikben egyenlő címkéket:

`ipaggmanip --prefix {{16}} {{path/to/file}}`

- A megadott bájtszámnál kisebb számmal rendelkező címkék eltávolítása és az ilyen címkék véletlenszerű mintájának kiadása:

`ipaggmanip --cut-smaller {{100}} --cull-labels {{5}} {{path/to/file}}`

- Az egyes címkék számának 1-re történő cseréje, ha az nem nulla:

`ipaggmanip --posterize {{path/to/file}}`
