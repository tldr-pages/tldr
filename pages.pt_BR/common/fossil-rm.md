# fossil rm

> Remove arquivos ou diretórios do controle de versão do Fossil.
> Veja também: `fossil forget`.
> Mais informações: <https://fossil-scm.org/home/help/rm>.

- Remove um arquivo ou diretório do controle de versão do Fossil:

`fossil rm {{caminho/para/arquivo_ou_diretório}}`

- Remove um arquivo ou diretório do controle de versão do Fossil e também o exclui do disco:

`fossil rm --hard {{caminho/para/arquivo_ou_diretório}}`

- Adiciona novamente todos os arquivos removidos e dos quais não se fez commit anteriormente ao controle de versão do Fossil:

`fossil rm --reset`
