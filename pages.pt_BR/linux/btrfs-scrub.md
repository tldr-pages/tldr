# btrfs scrub

> Varre os sistemas de arquivos btrfs para verificar a integridade dos dados.
> Recomenda-se fazer uma varredura uma vez por mês.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Começar uma varredura:

`sudo btrfs scrub start {{caminho/para/ponto_de_montagem_btrfs}}`

- Mostrar o status de uma varredura em andamento ou concluída:

`sudo btrfs scrub status {{caminho/para/ponto_de_montagem_btrfs}}`

- Cancelar uma varredura em andamento:

`sudo btrfs scrub cancel {{caminho/para/ponto_de_montagem_btrfs}}`

- Retomar uma varredura cancelada anteriormente:

`sudo btrfs scrub resume {{caminho/para/ponto_de_montagem_btrfs}}`

- Iniciar uma varredura, mas espera até que a varredura termine antes de sair:

`sudo btrfs scrub start -B {{caminho/para/ponto_de_montagem_btrfs}}`

- Iniciar uma varredura no modo silencioso (não imprime erros ou estatísticas):

`sudo btrfs scrub start -q {{caminho/para/ponto_de_montagem_btrfs}}`
