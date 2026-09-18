# ospp.vbs

> Instala, activa y gestiona versiones con licencia por volumen de los productos de Microsoft Office.
> Utiliza `cscript` para ejecutar este programa en la línea de comandos o `wscript` en la interfaz gráfica de usuario.
> Nota: Este comando puede anular, desactivar y/o eliminar tu volumen actual de versiones con licencia de productos de Office, por lo que te recomendamos que procedas con precaución.
> Vea también: `gethelpcmd-officeactivationscenario`.
> Más información: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- Instala una clave de producto (Nota: sustituye a la clave existente):

`cscript ospp.vbs /inpkey:{{clave_producto}}`

- Desinstalar una clave de producto instalada utilizando los últimos cinco dígitos de la clave de producto:

`cscript ospp.vbs /unpkey:{{dígitos_clave_producto}}`

- Establece un nombre de host KMS:

`cscript ospp.vbs /sethst:{{ip|nombre_host}}`

- Establece un puerto KMS:

`cscript ospp.vbs /setprt:{{puerto}}`

- Activa claves de producto de Office instaladas:

`cscript ospp.vbs /act`

- Muestra información de licencia para claves de producto instaladas:

`cscript ospp.vbs /dstatus`
