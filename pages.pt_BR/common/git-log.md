# git log

> Mostra um histórico de commits.
> Mais informações: <https://git-scm.com/docs/git-log>.

- Mostra a sequência de commits a partir do atual, em ordem cronológica reverse do repositório Git no diretório de trabalho atual:

`git log`

- Mostra o histórico de um arquivo ou diretório determinado, incluindo diferenças:

`git log -p {{caminho/para/arquivo_ou_diretório}}`

- Mostra uma visão geral do(s) arquivo(s) alterado(s) em cada commit:

`git log --stat`

- Mostra um grafo dos commits no branch atual usando apenas a primera linha de cada mensagem de commit:

`git log --oneline --graph`

- Mostra um grafo de todos os commits, etiquetas e branches em todo o repositório:

`git log --oneline --decorate --all --graph`

- Mostra apenas os commits cujas mensagem incluem uma determinada cadeia de caracteres (sem distinção entre maiúsculas e minúsculas):

`git log -i --grep {{cadeia_de_caracteres_para_pesquisa}}`

- Mostra os últimos N commits de um determinado autor:

`git log -n {{número}} --author={{autor}}`

- Mostra os commits entre duas datas(aaaa-mm-dd):

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
