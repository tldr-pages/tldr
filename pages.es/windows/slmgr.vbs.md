# slmgr.vbs

> Instala, activa y gestiona licencias de Windows.
> Este comando puede sobrescribir, desactivar y/o eliminar la licencia actual de Windows. Proceda con precaución.
> Más información: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- Mostrar[d] la [i]nformación actual de la [l]icencia de Windows:

`slmgr.vbs /dli`

- Mostrar[d] el [i]D de ins[t]alación del dispositivo actual. Útil para activación de licencia sin conexión:

`slmgr.vbs /dti`

- Mostrar la fecha y hora de caducidad e[xp]i[r]ación de la licencia actual:

`slmgr.vbs /xpr`

- [i]nstalar una nueva clave[k] de [p]roducto de licencia de Windows. Requiere privilegios de Administrador y sobrescribirá la licencia existente:

`slmgr.vbs /ipk {{product_key}}`

- [a]c[t]ivar la licencia de producto de Windows [o]nline. Requiere privilegios de Administrador:

`slmgr.vbs /ato`

- [a]c[t]ivar la licencia de [p]roducto de Windows offline (sin conexión). Requiere privilegios de Administrador y un ID de Confirmación proporcionado por el Centro de Activación de Productos Microsoft:

`slmgr.vbs /atp {{confirmation_id}}`

- Quitar [c] la clave [ky] de [p]roducto actual del registro de Windows. No desactiva ni desinstala la licencia, pero previene que la clave sea robada por programas maliciosos:

`slmgr.vbs /cpky`

- Desinstalar[u] la licencia actual (por su clave[k] de [p]roducto):

`slmgr.vbs /upk`
