# ospp.vbs

> Instala, activa y administra versiones con licencia por volumen de productos Microsoft Office.
> Nota: este comando puede anular, desactivar y/o eliminar tu volumen actual de versiones de productos Office con licencia, así que procede con cautela.
> Más información: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- Instala una clave de producto (Nota: sustituye a la clave existente):

`cscript ospp.vbs /inpkey:{{clave_producto}}`

- Desinstala una clave de producto instalada con los cinco últimos dígitos de la clave de producto:

`cscript ospp.vbs /unpkey:{{clave_producto}}`

- Establece un nombre de host KMS:

`cscript ospp.vbs /sethst:{{ip|nombre_host}}`

- Establece un puerto KMS:

`cscript ospp.vbs /setprt:{{puerto}}`

- Activa las claves de producto de Office instaladas:

`cscript ospp.vbs /act`

- Muestra la información de licencia de las claves de producto instaladas:

`cscript ospp.vbs /dstatus`
