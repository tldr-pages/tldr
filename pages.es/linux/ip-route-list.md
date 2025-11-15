# ip route list

> Subcomando de visualización para la gestión de la tabla de rutas IP.
> Más información: <https://manned.org/ip-route>.

- Muestra la tabla de enrutamiento `main`:

`ip {{[r|route]}} {{[l|list]}}`

- Muestra la tabla de enrutamiento principal (igual que el primer ejemplo):

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{main|254}}`

- Muestra la tabla de enrutamiento local:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{local|255}}`

- Muestra todas las tablas de enrutamiento:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{all|unspec|0}}`

- Lista solo las rutas de un dispositivo determinado:

`ip {{[r|route]}} {{[l|list]}} dev {{ethX}}`

- Lista las rutas dentro de un ámbito determinado:

`ip {{[r|route]}} {{[l|list]}} {{[s|scope]}} link`

- Muestra la caché de enrutamiento:

`ip {{[r|route]}} {{[l|list]}} {{[c|cache]}}`

- Muestra solo rutas IPv6 o IPv4:

`ip {{-6|-4}} {{[r|route]}}`
