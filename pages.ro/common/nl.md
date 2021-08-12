# nl

> Un utilitar pentru numerotarea liniilor, fie dintr-un fișier, fie din intrare standard.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/nl>

- Numărul de linii care nu sunt goale într-un fișier:

`nl {{file}}`

- Citiți din ieșirea standard:

`cat {{file}} | nl {{options}} -`

- Numărează doar liniile cu text imprimabil:

`nl -t {{file}}`

- Numarul tuturor liniilor, inclusiv liniile goale:

`nl -b a {{file}}`

- Numărează doar liniile caroseriei care se potrivesc cu un model de expresie regulată de bază (BRE):

`nl -b p'FooBar[0-9]' {{file}}`
