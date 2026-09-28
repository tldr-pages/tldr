# ip rule

> Gestión de la base de datos de políticas de enrutamiento IP.
> Vea también: `ip route`.
> Más información: <https://manned.org/ip-rule>.

- Muestra la política de enrutamiento:

`ip {{[ru|rule]}}`

- Crea una nueva regla de enrutamiento genérica con una prioridad mayor que `main`:

`sudo ip {{[ru|rule]}} {{[a|add]}} from all lookup {{table_id}}`

- Añade una nueva regla basada en las direcciones de origen de los paquetes:

`sudo ip {{[ru|rule]}} {{[a|add]}} from {{192.168.178.2/32}} lookup {{table_id}}`

- Añade una nueva regla basada en las direcciones de destino de los paquetes:

`sudo ip {{[ru|rule]}} {{[a|add]}} to {{192.168.178.2/32}} lookup {{table_id}}`

- Elimina una regla basada en las direcciones de origen de los paquetes:

`sudo ip {{[ru|rule]}} {{[d|delete]}} de {{192.168.178.2/32}}`

- Elimina todas las reglas de enrutamiento:

`sudo ip {{[ru|rule]}} {{[f|flush]}}`

- Guarda todas las reglas en un archivo:

`ip {{[ru|rule]}} {{[s|save]}} > {{ruta/a/ip_rules.dat}}`

- Restaura todas las reglas desde un archivo:

`sudo ip < {{ruta/a/ip_rules.dat}} {{[ru|rule]}} {{[r|restore]}}`
