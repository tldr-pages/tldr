# hydra

> Herramienta en línea para adivinar contraseñas.
> Entre los protocolos compatibles se incluyen FTP, HTTP(S), SMTP, SNMP, XMPP, SSH y muchos más.
> Más información: <https://manned.org/hydra>.

- Inicia el asistente de Hydra:

`hydra-wizard`

- Adivina credenciales SSH utilizando un nombre de usuario determinado y una lista de contraseñas:

`hydra -l {{nombre_de_usuario}} -P {{ruta/a/lista_de_palabras.txt}} {{ip_del_host}} {{ssh}}`

- Adivina credenciales de formularios web HTTPS utilizando dos listas específicas de nombres de usuario y contraseñas ("https_post_request" puede ser algo así como "usuario=^USER^&contraseña=^PASS^"):

`hydra -L {{ruta/a/nombre_de_usuarios.txt}} -P {{ruta/a/lista_de_palabras.txt}} {{ip_del_host}} {{https-post-form}} "{{url_sin_host}}:{{https_post_request}}:{{cadena_de_error_de_inicio_de_sesión}}"`

- Adivina credenciales FTP utilizando listas de nombres de usuario y contraseñas, especificando el número de subprocesos:

`hydra -L {{ruta/a/nombre_de_usuarios.txt}} -P {{ruta/a/lista_de_palabras.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- Adivina credenciales de MySQL utilizando un nombre de usuario y una lista de contraseñas, saliendo del proceso cuando se encuentre un conjunto de nombre de usuario y contraseña acordes:

`hydra -l {{nombre_de_usuario}} -P {{ruta/a/lista_de_palabras.txt}} -f {{host_ip}} {{mysql}}`

- Adivina las credenciales de RDP utilizando una lista de nombres de usuario y contraseñas, mostrando cada intento:

`hydra -l {{nombre_de_usuario}} -P {{ruta/a/lista_de_palabras.txt}} -V {{rdp://host_ip}}`

- Adivina credenciales IMAP en un rango de hosts utilizando una lista de pares de nombre de usuario y contraseña separados por dos puntos:

`hydra -C {{ruta/a/pares_nombre_de_usuario_contraseña.txt}} {{imap://[host_range_cidr]}}`

- Adivina las credenciales POP3 en una lista de hosts utilizando listas de nombres de usuario y contraseñas, y termina cuando se encuentra un nombre de usuario y contraseña:

`hydra -L {{ruta/a/nombre_de_usuarios.txt}} -P {{ruta/a/lista_de_palabras.txt}} -M {{ruta/a/hosts.txt}} -F {{pop3}}`
