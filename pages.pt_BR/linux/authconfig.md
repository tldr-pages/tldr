# authconfig

> Interface de linha comandos para configurar o sistema de autenticação.
> Mais informações: <https://manned.org/authconfig>.

- Exibe as configurações atuais (ou dry run):

`authconfig --test`

- Configura o servidor para utilizar diferentes algoritmos de hash para as senhas:

`authconfig --update --passalgo={{algoritmo}}`

- Habilita a autenticação via LDAP:

`authconfig --update --enableldapauth`

- Desabilita a autenticação via LDAP:

`authconfig --update --disableldapauth`

- Habilita o Network Information Service (NIS):

`authconfig --update --enablenis`

- Habilita Kerberos:

`authconfig --update --enablekrb5`

- Habilita a autenticação Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Habilita a autorização local:

`authconfig --update --enablelocauthorize`
