# authconfig

> Interface de linha comandos para configurar o sistema de autenticação.
> Mais informações: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

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
