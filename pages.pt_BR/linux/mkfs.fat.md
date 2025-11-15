# mkfs.fat

> Cria um sistema de arquivos MS-DOS dentro de uma partição.
> Mais informações: <https://manned.org/mkfs.fat>.

- Cria um sistema de arquivos fat dentro da partição 1 do dispositivo b (`sdb1`):

`mkfs.fat {{/dev/sdb1}}`

- Cria um sistema de arquivos com um nome de volume:

`mkfs.fat -n {{nome_de_volume}} {{/dev/sdb1}}`

- Cria um sistema de arquivos com um ID de volume:

`mkfs.fat -i {{id_de_volume}} {{/dev/sdb1}}`

- Usa 5 em vez de 2 tabelas de alocação de arquivos:

`mkfs.fat -f 5 {{/dev/sdb1}}`
