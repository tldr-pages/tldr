# authconfig

> Interface de linha comandos para configurar o sistema de autenticação.

- Exibir as configurações atuais (ou dry run):

`authconfig --test`

- Configurar o servidor para utilizar diferentes algoritmos de hash para as senhas:

`authconfig --update --passalgo={{algoritmo}}`

- Habilitar a autenticação via LDAP:

`authconfig --update --enableldapauth`

- Desabilitar a autenticação via LDAP:

`authconfig --update --disableldapauth`

- Habilitar o Network Information Service (NIS):

`authconfig --update --enablenis`

- Habilitar Kerberos:

`authconfig --update --enablekrb5`

- Habilitar a autenticação Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Habilitar a autorização local:

`authconfig --update --enablelocauthorize`
