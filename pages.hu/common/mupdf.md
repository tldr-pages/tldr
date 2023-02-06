# mupdf

> A MuPDF egy könnyű PDF, XPS és e-könyv megjelenítő. További információ: <https://www.mupdf.com>.

- PDF megnyitása az első oldalon:

`mupdf {{path/to/file}}`

- PDF megnyitása a 3. oldalon:

`mupdf {{path/to/file}} {{3}}`

- Jelszóval védett PDF megnyitása:

`mupdf -p {{password}} {{path/to/file}}`

- PDF megnyitása 72 DPI-ben megadott kezdeti nagyítási szinttel:

`mupdf -r {{72}} {{path/to/file}}`

- PDF megnyitása fordított színnel:

`mupdf -I {{path/to/file}}`

- PDF megnyitása pirosra színezve #FF0000 (hexadecimális színszintaxis RRGGBB):

`mupdf -C {{FF0000}}`

- PDF megnyitása élsimítás nélkül (0 = ki, 8 = legjobb):

`mupdf -A {{0}}`
