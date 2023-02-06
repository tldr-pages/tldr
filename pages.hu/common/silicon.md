# silicon

> A forráskód képének létrehozása. További információ: <https://github.com/Aloxaf/silicon>.

- Kép generálása egy adott forrásfájlból:

`silicon {{path/to/source_file}} --output {{path/to/output_image}}`

- Kép generálása egy adott programnyelvi szintaxis-kiemeléssel ellátott forrásfájlból (pl. `rust`, `py`, `js`, stb.):

`silicon {{path/to/source_file}} --output {{path/to/output_image}} --language {{language|extension}}`

- Kép generálása a `stdin`:

`{{command}} | silicon --output {{path/to/output_image}}`
