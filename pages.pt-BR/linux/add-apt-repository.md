# add-apt-repository

> Gerenciar definições de repositórios APT.

- Adiciona um repositório:

`add-apt-repository {{repository_spec}}`

- Remove um repositório:

`add-apt-repository --remove {{repository_spec}}`

- Adiciona um repositório e atualiza o cache do(s) pacote(s) deste repositório:

`add-apt-repository --update {{repository_spec}}`

- Adiciona um repositório e habilita o download do código fonte do(s) pacote(s) deste repositório:

`add-apt-repository --enable-source {{repository_spec}}`
