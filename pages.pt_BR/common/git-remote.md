# git remote

> Gerencia repositórios monitorados ("remotes").
> Mais informações: <https://git-scm.com/docs/git-remote>.

- Lista remotes existentes com seus nomes e URLs:

`git remote {{[-v|--verbose]}}`

- Mostra infomação de um remote específico:

`git remote show {{nome_do_remote}}`

- Adiciona um remote:

`git remote add {{nome_do_remote}} {{url_do_remote}}`

- Muda a URL de um remote (use `--add` para manter a URL existente):

`git remote set-url {{nome_do_remote}} {{nova_url}}`

- Mostra a URL de um remote:

`git remote get-url {{nome_do_remote}}`

- Remove um remote:

`git remote remove {{nome_do_remote}}`

- Renomeia um remote:

`git remote rename {{nome_antigo}} {{novo_nome}}`
