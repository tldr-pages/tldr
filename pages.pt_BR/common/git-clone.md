# git clone

> Clona um repositório existente.
> Mais informações: <https://git-scm.com/docs/git-clone>.

- Clona um repositório existente em um novo diretório (o diretório padrão é o nome do repositório):

`git clone {{local_do_repositório_remoto}} {{caminho/para/diretório}}`

- Clona um repositório existente e seus submódulos:

`git clone --recursive {{local_do_repositório_remoto}}`

- Clona somente o diretório `.git` de um repositório existente:

`git clone --no-checkout {{local_do_repositório_remoto}}`

- Clona um repositório local:

`git clone --local {{caminho/para/repositório/local}}`

- Clona de forma silenciosa:

`git clone --quiet {{local_do_repositório_remoto}}`

- Clona um repositório existente buscando somente os 10 commits mais recentes na branch padrão (útil para salvar tempo):

`git clone --depth {{10}} {{local_do_repositório_remoto}}`

- Clona um repositório existente buscando somente uma branch específica:

`git clone --branch {{nome}} --single-branch {{local_do_repositório_remoto}}`

- Clona um repositório existente usando um comando SSH específico:

`git clone --config core.sshCommand="{{ssh -i caminho/para/chave_ssh_privada}}" {{local_do_repositório_remoto}}`
