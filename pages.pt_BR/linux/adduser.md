# adduser

> Utilitário para criação de novos usuários.
> Mais informações: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Cria um novo usuário, o seu diretório na pasta home e solicita o preenchimento da sua senha:

`adduser {{nome_do_usuario}}`

- Cria um novo usuário sem o seu diretório na pasta home:

`adduser --no-create-home {{nome_do_usuario}}`

- Cria um novo usuário especificando a localização do seu diretório:

`adduser --home {{caminho_da_pasta_do_usuario}} {{nome_do_usuario}}`

- Cria um novo usuário e configura o seu shell de login:

`adduser --shell {{caminho_para_o_shell}} {{nome_do_usuario}}`

- Cria um novo usuário e atribuí-lo a um grupo:

`adduser --ingroup {{grupo}} {{nome_do_usuario}}`
