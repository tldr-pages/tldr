# lzop

> Comprimare sau decomprimare fişiere cu compresie LZO.
> Mai multe informaţii: <https://www.lzop.org/>

- Comprimați un fișier într-un fișier nou cu sufixul `.lzo':

`lzop {{file}}`

- Decomprima un fișier:

`lzop -d {{file}}.lzo`

- Comprimați un fișier, specificând nivelul de compresie. 0 = Cel mai rău, 9 = Cel mai bun (Nivelul implicit este 3):

`lzop -{{level}} {{file}}`
