# btrfs scrub

> Varre os sistemas de arquivos btrfs para verificar a integridade dos dados.
> Recomenda-se fazer uma varredura uma vez por mês.
> Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Começar uma varredura:

`sudo btrfs scrub start {{caminho/para/ponto_de_montagem_btrfs}}`

- Mostra o status de uma varredura em andamento ou concluída:

`sudo btrfs scrub status {{caminho/para/ponto_de_montagem_btrfs}}`

- Cancela uma varredura em andamento:

`sudo btrfs scrub cancel {{caminho/para/ponto_de_montagem_btrfs}}`

- Retoma uma varredura cancelada anteriormente:

`sudo btrfs scrub resume {{caminho/para/ponto_de_montagem_btrfs}}`

- Inicia uma varredura, mas espera até que a varredura termine antes de sair:

`sudo btrfs scrub start -B {{caminho/para/ponto_de_montagem_btrfs}}`

- Inicia uma varredura no modo silencioso (não imprime erros ou estatísticas):

`sudo btrfs scrub start -q {{caminho/para/ponto_de_montagem_btrfs}}`
