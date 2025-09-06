# dvc checkout

> Registra a saída de arquivos e diretórios de dados vindos do cache.
> Mais informações: <https://dvc.org/doc/command-reference/checkout>.

- Registra a saída de todos os arquivos e diretórios de dados:

`dvc checkout`

- Registra a saída da última versão de um alvo específico:

`dvc checkout {{alvo}}`

- Registra a saída de versão específica de um alvo de um commit/tag/branch Git:

`git checkout {{hash_do_commit|tag|branch}} {{alvo}} && dvc checkout {{alvo}}`
