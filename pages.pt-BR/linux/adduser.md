# adduser

> Utilitário para criação de novos usuários.

- Cria um novo usuário, o seu diretório na pasta home e solicita o preenchimento da sua senha:

`adduser {{username}}`

- Cria um novo usuário sem o seu diretório na pasta home:

`adduser --no-create-home {{username}}`

- Cria um novo usuário especificando a localização do seu diretório:

`adduser --home {{path/to/home}} {{username}}`

- Cria um novo usuário e configura o seu shell de login:

`adduser --shell {{path/to/shell}} {{username}}`

- Cria um novo usuário e o atribui a um grupo específico:

`adduser --ingroup {{group}} {{username}}`
