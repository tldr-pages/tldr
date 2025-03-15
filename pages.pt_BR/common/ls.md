# ls

> Lista o conteúdo de um diretório.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Lista arquivos um por linha:

`ls -1`

- Lista todos os arquivos, incluindo arquivos ocultos:

`ls {{[-a|--all]}}`

- Lista todos os arquivos, com o final `/` adicionado aos nomes dos diretórios:

`ls {{[-F|--classify]}}`

- Lista todos os arquivos em formato longo (permissões, dono, tamanho e data de modificação):

`ls {{[-la|--all -l]}}`

- Lista em formato longo com tamanho exibido usando unidades legíveis para humanos (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Lista em formato longo ordenados por tamanhos (decrescente):

`ls {{-lSR|-lS --recursive}}`

- Lista todos os arquivos em formato longo, ordenados por data de modificação (mais antigo primeiro):

`ls {{[-ltr|-lt --reverse]}}`

- Lista apenas diretórios:

`ls {{[-d|--directory]}} */`
