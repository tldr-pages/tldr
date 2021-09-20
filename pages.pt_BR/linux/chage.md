# chage

> Gerencia informações de expiração de conta e senha do usuário.
> Mais informações: <https://manned.org/chage>.

- Exibir as informações referentes a senha do usuário:

`chage --list {{nome_do_usuario}}`

- Habilitar a expiração da senha do usuário em 10 dias:

`sudo chage --maxdays {{10}} {{nome_do_usuario}}`

- Desabilitar a expiração da senha do usuário:

`sudo chage --maxdays {{-1}} {{nome_do_usuario}}`

- Definir a data de expiração da conta do usuário:

`sudo chage --expiredate {{YYYY-MM-DD}} {{nome_do_usuario}}`

- Obrigar o usuário a alterar sua senha no próximo login:

`sudo chage --lastday {{0}} {{nome_do_usuario}}`
