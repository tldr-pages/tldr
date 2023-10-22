# mkfs.btrfs

> Crie um sistema de arquivos btrfs.
> O padrão é `raid1`, que especifica 2 cópias de um determinado bloco de dados espalhados por 2 dispositivos diferentes.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Criar um sistema de arquivos btrfs em um único dispositivo:

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- Criar um sistema de arquivos btrfs em vários dispositivos com raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- Definir um rótulo para o sistema de arquivos:

`sudo mkfs.btrfs --label "{{rótulo}}" {{/dev/sda}} [{{/dev/sdN}}]`
