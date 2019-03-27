# chage

> Gerencia informações de expiração da conta e senha do usuário.

- Exibe as informações referentes a senha do usuário:

`chage -l {{user_name}}`

- Habilita a expiração da senha em 10 dias:

`sudo chage -M {{10}} {{user_name}}`

- Desabilita a expiração de senha:

`sudo chage -M -1 {{user_name}}`

- Define a data de expiração da conta:

`sudo chage -E {{YYYY-MM-DD}}`

- Obriga o usuário a alterar sua senha no próximo login:

`sudo chage -d 0`
