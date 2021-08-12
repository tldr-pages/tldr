# xz

> Comprimare sau decompresie fișiere.xz și .lzma.
> Mai multe informaţii: <https://tukaani.org/xz/format.html>

- Comprimați un fișier în formatul de fișier xz:

`xz {{file}}`

- Decomprima un fișier xz:

`xz -d {{file.xz}}`

- Comprimați un fișier în formatul de fișier lzma:

`xz --format=lzma {{file}}`

- Decomprima un fișier lzma:

`xz -d --format=lzma {{file.lzma}}`

- Decomprima un fișier și scrie la stdout:

`xz -dc {{file.xz}}`

- Comprimați un fișier, dar nu ștergeți originalul:

`xz -k {{file}}`

- Comprimați un fișier utilizând cea mai rapidă compresie:

`xz -0 {{file}}`

- Comprimați un fișier folosind cea mai bună compresie:

`xz -9 {{file}}`
