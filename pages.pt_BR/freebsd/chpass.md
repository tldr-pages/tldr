# chpass

> Adiciona ou altera informação de usuário do banco de dados, incluindo login shell e senha.
> Veja também: `passwd`.
> Mais informações: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Adiciona ou altera informação de usuário do banco de dados para o usuário atual interativamente:

`su -c chpass`

- Define uma [s]hell de login para o usuário atual:

`chpass -s {{caminho/para/shell}}`

- Define uma [s]hell de login para um usuário específico:

`chpass -s {{caminho/para/shell}} {{nome_do_usuário}}`

- Altera o tempo de [e]xpiração da conta (Unix epoch):

`su -c 'chpass -e {{tempo}} {{nome_do_usuário}}'`

- Altera a senha de um usuário:

`su -c 'chpass -p {{senha_criptografada}} {{nome_do_usuário}}'`

- Especifica [h]ostname ou endereço de um servidor NIS para consulta:

`su -c 'chpass -h {{hostname}} {{nome_do_usuário}}'`

- Especifica um [d]omínio NIS específico (nome do domínio do sistema por padrão):

`su -c 'chpass -d {{domínio}} {{nome_do_usuário}}'`
