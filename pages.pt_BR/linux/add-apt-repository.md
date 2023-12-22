# add-apt-repository

> Gerenciar definições de repositórios APT.
> Mais informações: <https://manned.org/apt-add-repository>.

- Adiciona um repositório:

`add-apt-repository {{especificacao_do_repositorio}}`

- Remove um repositório:

`add-apt-repository --remove {{especificacao_do_repositorio}}`

- Adiciona um repositório e atualiza o cache do(s) pacote(s) deste repositório:

`add-apt-repository --update {{especificacao_do_repositorio}}`

- Adiciona um repositório e habilita o download do código fonte do(s) pacote(s) deste repositório:

`add-apt-repository --enable-source {{especificacao_do_repositorio}}`
