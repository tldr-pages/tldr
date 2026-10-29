# chage

> Gerencia informações de expiração de conta e senha do usuário.
> Mais informações: <https://manned.org/chage>.

- Exibe as informações referentes a senha do usuário:

`chage {{[-l|--list]}} {{nome_do_usuario}}`

- Habilita a expiração da senha do usuário em 10 dias:

`sudo chage {{[-M|--maxdays]}} 10 {{nome_do_usuario}}`

- Desabilita a expiração da senha do usuário:

`sudo chage {{[-M|--maxdays]}} -1 {{nome_do_usuario}}`

- Define a data de expiração da conta do usuário:

`sudo chage {{[-E|--expiredate]}} {{YYYY-MM-DD}} {{nome_do_usuario}}`

- Obriga o usuário a alterar sua senha no próximo login:

`sudo chage {{[-d|--lastday]}} 0 {{nome_do_usuario}}`
