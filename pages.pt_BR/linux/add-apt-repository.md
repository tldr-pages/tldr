# add-apt-repository

> Gerenciar definições de repositórios APT.
> Mais informações: <https://manned.org/apt-add-repository>.

- Adicionar um repositório:

`add-apt-repository {{especificacao_do_repositorio}}`

- Remover um repositório:

`add-apt-repository --remove {{especificacao_do_repositorio}}`

- Adicionar um repositório e atualizar o cache do(s) pacote(s) deste repositório:

`add-apt-repository --update {{especificacao_do_repositorio}}`

- Adicionar um repositório e habilitar o download do código fonte do(s) pacote(s) deste repositório:

`add-apt-repository --enable-source {{especificacao_do_repositorio}}`
