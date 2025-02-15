# smbcacls

> Visualiza y manipula ACLs de Windows en recursos compartidos SMB.
> Parte de la suite Samba.
> Más información: <https://www.samba.org/samba/docs/current/man-html/smbcacls.1.html>.

- Muestra las ACLs de un archivo o directorio en un recurso compartido SMB remoto:

`smbcacls //{{servidor}}/{{compartido}} {{ruta/al/archivo_o_directorio}} --user {{dominio\\nombre_usuario}}%{{contraseña}}`

- Establece una nueva ACL para un archivo en un recurso compartido SMB remoto (reemplaza `"ACL:..."` con una especificación ACL válida de Windows):

`smbcacls //{{servidor}}/{{compartido}} {{ruta/al/archivo}} --user {{dominio\\nombre_usuario}}%{{contraseña}} "ACL:{{DACL}}"`

- Elimina todas las entradas ACL existentes y establece una nueva ACL:

`smbcacls //{{servidor}}/{{compartido}} {{ruta/al/archivo}} --user {{dominio\\nombre_usuario}}%{{contraseña}} "RESET" "ACL:{{DACL}}"`

- Especifica un grupo de trabajo (o dominio) alternativo y hace que el programa solicite una contraseña de forma interactiva:

`smbcacls //{{servidor}}/{{compartido}} {{ruta/al/archivo}} --user {{nombre_usuario}} --workgroup {{grupo_de_trabajo}}`
