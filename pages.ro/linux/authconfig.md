# authconfig

> O interfață CLI pentru configurarea resurselor de autentificare a sistemului.
> Mai multe informaţii: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>

- Afișează configurația curentă (sau a alerga uscat):

`authconfig --test`

- Configurați serverul pentru a utiliza un algoritm de hash parolă diferit:

`authconfig --update --passalgo={{algorithm}}`

- Activează autentificarea LDAP:

`authconfig --update --enableldapauth`

- Dezactivați autentificarea LDAP:

`authconfig --update --disableldapauth`

- Activați serviciul de informații de rețea (NIS):

`authconfig --update --enablenis`

- Activează Kerberos:

`authconfig --update --enablekrb5`

- Activați autentificarea Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Activează autorizarea locală:

`authconfig --update --enablelocauthorize`
