# authconfig

> Configura los recursos de autenticación del sistema.
> Más información: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- Muestra la configuración actual (o realiza una simulación):

`authconfig --test`

- Configura el servidor para usar un algoritmo de hash de contraseñas diferente:

`authconfig --update --passalgo={{algoritmo}}`

- Habilita la autenticación LDAP:

`authconfig --update --enableldapauth`

- Deshabilita la autenticación LDAP:

`authconfig --update --disableldapauth`

- Habilita el servicio de información de red (NIS):

`authconfig --update --enablenis`

- Habilita Kerberos:

`authconfig --update --enablekrb5`

- Habilita la autenticación Winbind (Active Directory):

`authconfig --update --enablewinbindauth`

- Habilita la autorización local:

`authconfig --update --enablelocauthorize`
