# btrfs balance

> Balanceia grupos de blocos em um sistema de arquivos btrfs.
> Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-balance>.

- Mostra o status de uma operação balance em execução ou pausada:

`sudo btrfs balance status {{caminho/para/sistema_de_arquivos_btrfs}}`

- Balanceia todos os grupos de blocos (lento; reescreve todos os blocos no sistema de arquivos):

`sudo btrfs balance start {{caminho/para/sistema_de_arquivos_btrfs}}`

- Balanceia grupos de blocos de dados com menos de 15% de utilização, executando a operação em segundo plano:

`sudo btrfs balance start --bg -dusage={{15}} {{caminho/para/sistema_de_arquivos_btrfs}}`

- Balanceia um máximo de 10 partes de metadados com menos de 20% de utilização e pelo menos 1 parte em um determinado dispositivo `devid` (consulte `btrfs filesystem show`):

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{caminho/para/sistema_de_arquivos_btrfs}}`

- Converte blocos de dados para raid6 e metadados para raid1c3 (veja mkfs.btrfs(8) para perfis):

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{caminho/para/sistema_de_arquivos_btrfs}}`

- Converte blocos de dados para raid1, pulando pedaços já convertidos (por exemplo, após uma operação de conversão cancelada anterior):

`sudo btrfs balance start -dconvert={{raid1}},soft {{caminho/para/sistema_de_arquivos_btrfs}}`

- Cancela, pausa ou retoma uma operação de balanceamento em execução ou pausada:

`sudo btrfs balance {{cancel|pause|resume}} {{caminho/para/sistema_de_arquivos_btrfs}}`
