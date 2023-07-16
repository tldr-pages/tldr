# ssh-add

> Gerencia as chaves SSH carregadas no ssh-agent.
> Certifique-se de que o ssh-agent esteja em execução para que as chaves sejam carregadas nele.
> Mais informações: <https://man.openbsd.org/ssh-add>.

- Adicionar as chaves SSH padrão em `~/.ssh` ao ssh-agent:

`ssh-add`

- Adicionar uma chave específica ao ssh-agent:

`ssh-add {{caminho/para/chave_privada}}`

- Listar as impressões digitais das chaves carregadas atualmente:

`ssh-add -l`

- Excluir uma chave do ssh-agent:

`ssh-add -d {{caminho/para/chave_privada}}`

- Excluir todas as chaves carregadas atualmente do ssh-agent:

`ssh-add -D`

- Adicionar uma chave ao ssh-agent e ao keychain:

`ssh-add -K {{caminho/para/chave_privada}}`
