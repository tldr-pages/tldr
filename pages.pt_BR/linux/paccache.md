# paccache

> Um utilitário de limpeza do cache do `pacman`.
> Mais informações: <https://manned.org/paccache>.

- Remove tudo, exceto as 3 versões mais recentes do cache do `pacman`:

`paccache {{[-r|--remove]}}`

- Define o número de versões do pacote para manter:

`paccache {{[-rk|--remove --keep]}} {{num_versoes}}`

- Executa um teste e mostra o número de pacotes candidatos para exclusão:

`paccache {{[-d|--dryrun]}}`

- Move os pacotes candidatos para um diretório ao invés de excluí-los:

`paccache {{[-m|--move]}} {{caminho/para/diretorio}}`
