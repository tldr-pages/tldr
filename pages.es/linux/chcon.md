# chcon

> Cambia el contexto de seguridad de SELinux de uno o varios archivos o directorios.
> Vea también: `secon`, `restorecon`, `semanage-fcontext`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- Vea el contexto de seguridad de un archivo:

`ls {{[-lZ|-l --context]}} {{ruta/al/archivo}}`

- Cambia el contexto de seguridad de un archivo de destino utilizando un archivo de referencia:

`chcon --reference {{archivo_de_referencia}} {{archivo_de_destino}}`

- Cambia el contexto de seguridad completo de SELinux de un archivo:

`chcon {{usuario}}:{{rol}}:{{tipo}}:{{rango/nivel}} {{nombre_archivo}}`

- Cambia únicamente la parte de usuario del contexto de seguridad de SELinux:

`chcon {{[-u|--user]}} {{usuario}} {{nombre_del_archivo}}`

- Cambia únicamente la parte de rol del contexto de seguridad de SELinux:

`chcon {{[-r|--role]}} {{rol}} {{nombre_del_archivo}}`

- Cambia únicamente la parte de tipo del contexto de seguridad de SELinux:

`chcon {{[-t|--type]}} {{tipo}} {{nombre_del_archivo}}`

- Cambia únicamente la parte de rango/nivel del contexto de seguridad de SELinux:

`chcon {{[-l|--range]}} {{rango/nivel}} {{nombre_del_archivo}}`
