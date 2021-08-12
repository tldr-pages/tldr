# pigz

> Utilitar de compresie zlib multifiletat.
> Mai multe informaţii: <https://github.com/madler/pigz>

- Comprimați un fișier cu opțiuni implicite:

`pigz {{filename}}`

- Comprimați un fișier utilizând cea mai bună metodă de compresie:

`pigz -9 {{filename}}`

- Comprimați un fișier fără compresie și 4 procesoare:

`pigz -0 -p{{4}} {{filename}}`

- Comprimați un director folosind tar:

`tar cf - {{path/to/directory}} | pigz > {{filename}}.tar.gz`

- Decomprima un fișier:

`pigz -d {{archive.gz}}`

- Listează conținutul unei arhive:

`pigz -l {{archive.tar.gz}}`
