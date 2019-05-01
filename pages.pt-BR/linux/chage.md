# chage

> Gerencia informações de expiração de conta e senha do usuário.

- Exibir as informações referentes a senha do usuário:

`chage -l {{nome_do_usuario}}`

- Habilitar a expiração da senha do usuário em 10 dias:

`sudo chage -M {{10}} {{nome_do_usuario}}`

- Desabilitar a expiração da senha do usuário:

`sudo chage -M -1 {{nome_do_usuario}}`

- Definir a data de expiração da conta do usuário:

`sudo chage -E {{YYYY-MM-DD}}`

- Obrigar o usuário a alterar sua senha no próximo login:

`sudo chage -d 0`
