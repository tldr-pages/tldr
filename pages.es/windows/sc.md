# sc

> Comunicación con el Administrador de Control de Servicios y los servicios.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Muestra el estado de un servicio (al no nombrar un servicio se listan todos los servicios):

`sc.exe query {{nombre_del_servicio}}`

- Inicia un servicio asincrónicamente:

`sc.exe create {{nombre_del_servicio}} binpath= {{ruta\al\binario_del_servicio}}`

- Detiene un servicio asincrónicamente:

`sc.exe delete {{nombre_del_servicio}}`

- Establece el tipo de servicio:

`sc.exe config {{nombre_del_servicio}} type= {{tipo_de_servicio}}`
