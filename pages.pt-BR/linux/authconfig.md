# authconfig

> Uma interface de linhas comando para configurar o systema de autenticação.

- Exibe as configurações atuais (ou dry run):

`authconfig --test`

- Configura ao servidor para utilizar diferentes algoritmos de hash para as senhas:

`authconfig --update --passalgo={{algorithm}}`

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
