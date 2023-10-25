# git commit

> Faz um commit dos arquivos no repositório.
> Mais informações: <https://git-scm.com/docs/git-commit>.

- Faz um commit com os arquivos preparados no repositório com uma mensagem:

`git commit --message "{{mensagem}}"`

- Faz um commit com os arquivos preparados com uma mensagem lida de um arquivo:

`git commit --file {{caminho/para/arquivo_de_mensagem_do_commit}}`

- Prepara automaticamente todos os arquivos modificados e excluídos e faz o commit com uma mensagem:

`git commit --all --message "{{mensagem}}"`

- Faz um commit com os arquivos preparados e assina-os com a chave GPG especificada (ou a definida no arquivo de configuração se nenhum argumento for especificado):

`git commit --gpg-sign {{id_da_chave}} --message "{{mensagem}}"`

- Atualiza o último commit adicionando as alterações atualmente preparadas, alterando o hash do commit:

`git commit --amend`

- Faz um commit apenas de arquivos específicos (já preparados):

`git commit {{caminho/para/arquivo1}} {{caminho/para/arquivo2}}`

- Cria um commit, mesmo se não haja arquivos preparados:

`git commit --message "{{mensagem}}" --allow-empty`
