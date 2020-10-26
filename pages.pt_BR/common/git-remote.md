# git remote

> Gerencia repositórios monitorados ("remotes").
> Mais informações: <https://git-scm.com/docs/git-remote>.

- Mostre uma lista de remotes existentes, seus nomes e URL:

`git remote -v`

- Mostra infomação de um remote específico:

`git remote show {{nome_do_remote}}`

- Adiciona um remote:

`git remote add {{nome_do_remote}} {{url_do_remote}}`

- Muda a URL de um remote (use `--add` para manter a URL existente):

`git remote set-url {{nome_do_remote}} {{nova_url}}`

- Remove um remote:

`git remote remove {{nome_do_remote}}`

- Renomeia um remote:

`git remote rename {{nome_antigo}} {{novo_nome}}`
