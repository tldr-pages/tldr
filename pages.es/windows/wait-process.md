# Wait-Process

> Espera a que los procesos se detengan antes de aceptar más entradas.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/wait-process>.

- Detener un proceso y esperar:

`Stop-Process -Id {{id_del_proceso}}; Wait-Process -Id {{id_del_proceso}}`

- Esperar a que los procesos terminen durante un tiempo especificado:

`Wait-Process -Name {{nombre_del_proceso}} -Timeout {{30}}`
