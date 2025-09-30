# Test-NetConnection

> Muestra información de diagnóstico de una conexión.
> Este comando solo se puede utilizar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- Probar una conexión y mostrar resultados detallados:

`Test-NetConnection -InformationLevel Detailed`

- Probar una conexión a un host remoto con un número de puerto específico:

`Test-NetConnection -ComputerName {{ip_o_nombre_del_host}} -Port {{número_de_puerto}}`
