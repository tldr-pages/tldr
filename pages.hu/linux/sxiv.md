# sxiv

> Simple X Image Viewer. További információ: <https://github.com/muennich/sxiv>.

- Kép megnyitása:

`sxiv {{path/to/file}}`

- Kép megnyitása teljes képernyős módban:

`sxiv -f {{path/to/file}}`

- Képek új sorokkal elválasztott listájának megnyitása, fájlnevek beolvasása a standard bemenetről:

`echo {{path/to/file}} | sxiv -i`

- Képek szóközzel elválasztott listájának megnyitása diavetítésként:

`sxiv -S {{seconds}} {{path/to/file}}`

- Képek szóközzel elválasztott listájának megnyitása miniatűr módban:

`sxiv -t {{path/to/file}}`
