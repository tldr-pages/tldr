# ip rule

> Gestión de bases de datos de políticas de enrutamiento IP.
> Más información: <https://manned.org/ip-rule>.

- Muestra la política de enrutamiento:

`ip {{[ru|rule]}}`

- Agrega una nueva regla basada en las direcciones fuente de paquetes:

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}}`

- Añade una nueva regla basada en direcciones de destino de paquetes:

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}}`

- Elimina una regla basada en las direcciones fuente de paquetes:

`sudo ip {{[ru|rule]}} {{[d|delete]}} from {{192.168.178.2/32}}`

- Elimina una regla basada en las direcciones de destino de paquetes:

`sudo ip {{[ru|rule]}} {{[d|delete]}} to {{192.168.178.2/32}}`

- Limpia todas las reglas eliminadas:

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- Guarda todas las reglas en un archivo:

`ip {{[ru|rule]}} {{[s|save]}} > {{ruta/a/reglas_ip.dat}}`

- Restaura todas las reglas desde un archivo:

`sudo ip {{[ru|rule]}} {{[r|restore]}} < {{ruta/a/reglas_ip.dat}}`
