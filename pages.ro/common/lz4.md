# lz4

> Comprimare sau decompresie fișiere.lz4.
> Mai multe informaţii: <https://github.com/lz4/lz4>

- Comprimare fișier:

`lz4 {{file}}`

- Decomprima un fișier:

`lz4 -d {{file.lz4}}`

- Decomprima un fișier și scrie la stdout:

`lz4 -dc {{file.lz4}}`

- Pachet și comprima un director și conținutul său:

`tar cvf - {{path/to/directory}} | lz4 - {{dir.tar.lz4}}`

- Decomprima și despachetați un director și conținutul său:

`lz4 -d {{dir.tar.lz4}} | tar -xv`

- Comprimați un fișier folosind cea mai bună compresie:

`lz4 -9 {{file}}`
