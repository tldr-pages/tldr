# apg

> Tetszőlegesen összetett véletlenszerű jelszavakat hoz létre. További információ: <https://manned.org/apg>.

- Véletlenszerű jelszavak létrehozása (az alapértelmezett jelszó hossza 8):

`apg`

- Hozzon létre egy jelszót, amely legalább 1 szimbólumot (S), 1 számot (N), 1 nagybetűt (C), 1 kisbetűt (L) tartalmaz:

`apg -M SNCL`

- Hozzon létre egy 16 karakteres jelszót:

`apg -m {{16}}`

- Hozzon létre egy legfeljebb 16 karakteres jelszót:

`apg -x {{16}}`

- Olyan jelszó létrehozása, amely nem szerepel a szótárban (a szótárfájlt meg kell adni):

`apg -r {{dictionary_file}}`
