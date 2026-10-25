# slmgr.vbs

> Instala, activa y gestiona licencias de Windows.
> Este comando puede sobrescribir, desactivar y/o eliminar la licencia actual de Windows. Proceda con precaución.
> Más información: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- Muestra[d] la [i]nformación actual de la [l]icencia de Windows:

`cscript slmgr.vbs /dli`

- Muestra[d] el [i]D de ins[t]alación del dispositivo actual. Útil para activación de licencia sin conexión:

`cscript slmgr.vbs /dti`

- Muestra la fecha y hora de caducidad e[xp]i[r]ación de la licencia actual:

`cscript slmgr.vbs /xpr`

- [i]nstala una nueva clave[k] de [p]roducto de licencia de Windows. Requiere privilegios de Administrador y sobrescribirá la licencia existente:

`cscript slmgr.vbs /ipk {{product_key}}`

- [a]c[t]iva la licencia de producto de Windows [o]nline. Requiere privilegios de Administrador:

`cscript slmgr.vbs /ato`

- [a]c[t]iva la licencia de [p]roducto de Windows offline (sin conexión). Requiere privilegios de Administrador y un ID de Confirmación proporcionado por el Centro de Activación de Productos Microsoft:

`cscript slmgr.vbs /atp {{confirmation_id}}`

- Quita [c] la clave [ky] de un [p]roducto actual del registro de Windows. No desactiva ni desinstala la licencia, pero previene que la clave sea robada por programas maliciosos:

`cscript slmgr.vbs /cpky`

- Desinstala[u] la licencia actual (por su clave[k] de [p]roducto):

`cscript slmgr.vbs /upk`
