# mytop

> A MySQL szerver teljesítményére vonatkozó információk megjelenítése, mint például a `top`. További információ: <http://jeremy.zawodny.com/mysql/mytop/mytop.html>.

- Indítsa el a mytop-ot:

`mytop`

- Csatlakozás megadott felhasználónévvel és jelszóval:

`mytop -u {{user}} -p {{password}}`

- Csatlakozás megadott felhasználónévvel (a felhasználónak jelszót kell megadnia):

`mytop -u {{user}} --prompt`

- Ne jelenítsen meg üres (alvó) szálakat:

`mytop -u {{user}} -p {{password}} --noidle`
