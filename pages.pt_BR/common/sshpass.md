# sshpass

> Um provedor de senha SSH.
> Ele funciona criando um TTY, inserindo a senha nele e, em seguida, redirecionando `stdin` para a sessão SSH.
> Mais informações: <https://manned.org/sshpass>.

- Conecta a um servidor remoto usando uma senha fornecida em um descritor de arquivo (neste caso, `stdin`):

`sshpass -d {{0}} ssh {{usuário}}@{{hostname}}`

- Conecta a um servidor remoto com a senha fornecida como opção e aceita automaticamente chaves SSH desconhecidas:

`sshpass -p {{senha}} ssh -o StrictHostKeyChecking=no {{usuário}}@{{hostname}}`

- Conecta a um servidor remoto usando a primeira linha de um arquivo como senha, aceita automaticamente chaves SSH desconhecidas e executa um comando:

`sshpass -f {{caminho/para/arquivo}} ssh -o StrictHostKeyChecking=no {{usuário}}@{{hostname}} "{{comando}}"`
