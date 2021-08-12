# zstd

> Comprimare sau decomprimare fişiere cu compresie Zstandard.
> Mai multe informaţii: <https://github.com/facebook/zstd>

- Comprimați un fișier într-un fișier nou cu sufixul `.zst:

`zstd {{file}}`

- Decomprima un fișier:

`zstd -d {{file}}.zst`

- Decomprima la stdout:

`zstd -dc {{file}}.zst`

- Comprimați un fișier care specifică nivelul de compresie, unde 1 = cel mai rapid, 19 = cel mai lent și 3 = implicit:

`zstd -{{level}} {{file}}`

- Deblocați niveluri mai ridicate de compresie (până la 22) folosind mai multă memorie (atât pentru compresie și decompresie):

`zstd --ultra -{{level}} {{file}}`
