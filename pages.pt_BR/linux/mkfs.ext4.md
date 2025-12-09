# mkfs.ext4

> Cria um sistema de arquivos ext4 dentro de uma partição.
> Mais informações: <https://manned.org/mkfs.ext4>.

- Cria um sistema de arquivos ext4 dentro da partição 1 no dispositivo b (`sdb1`):

`sudo mkfs.ext4 {{/dev/sdb1}}`

- Cria um sistema de arquivo ext4 com um rótulo de volume:

`sudo mkfs.ext4 -L {{rótulo_de_volume}} {{/dev/sdb1}}`
