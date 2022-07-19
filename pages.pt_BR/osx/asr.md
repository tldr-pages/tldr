# asr

> Restaurar (copiar) uma imagem de disco em um volume.
> O nome do comando significa Apple Software Restore.
> Mais informações: <https://www.unix.com/man-page/osx/8/asr/>.

- Restaurar uma imagem de disco para um volume de destino:

`sudo asr restore --source {{nome_da_imagem}}.dmg --target {{caminho/para/volume}}`

- Apagar o volume de destino antes de restaurar:

`sudo asr restore --source {{nome_da_imagem}}.dmg --target {{caminho/para/volume}} --erase`

- Ignorar a verificação após a restauração:

`sudo asr restore --source {{nome_da_imagem}}.dmg --target {{caminho/para/volume}} --noverify`

- Clonar volumes sem o uso de uma imagem de disco intermediária:

`sudo asr restore --source {{caminho/para/volume}} --target {{caminho/para/volume_clonado}}`
