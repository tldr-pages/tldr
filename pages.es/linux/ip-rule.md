# ip rule

> Gestión de bases de datos de políticas de enrutamiento IP.
> Más información: <https://manned.org/ip-rule>.

- Muestra la política de enrutamiento:

`ip {{[ru|rule]}} {{show|list}}`

- Agrega una nueva regla basada en las direcciones fuente de paquetes:

`sudo ip {{[ru|rule]}} add from {{192.168.178.2/32}}`

- Añade una nueva regla basada en direcciones de destino de paquetes:

`sudo ip {{[ru|rule]}} add to {{192.168.178.2/32}}`

- Elimina una regla basada en las direcciones fuente de paquetes:

`sudo ip {{[ru|rule]}} delete from {{192.168.178.2/32}}`

- Elimina una regla basada en las direcciones de destino de paquetes:

`sudo ip {{[ru|rule]}} delete to {{192.168.178.2/32}}`

- Limpia todas las reglas eliminadas:

`ip {{[ru|rule]}} flush`

- Guarda todas las reglas en un archivo:

`ip {{[ru|rule]}} save > {{ruta/a/reglas_ip.dat}}`

- Restaura todas las reglas desde un archivo:

`ip {{[ru|rule]}} restore < {{ruta/a/reglas_ip.dat}}`
