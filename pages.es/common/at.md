# at

> Ejecuta los comandos una vez en otro momento.
> Los resultados se enviarán al correo del usuario.
> Más información: <https://manned.org/at>.

- Crea comandos interactivamente y los ejecuta en 5 minutos (pulsa `<Ctrl d>` cuando termines)::

`at now + 5 minutes`

- Crea comandos interactivamente y los ejecuta a una hora determinada:

`at {{hh:mm}}`

- Ejecuta un comando de `stdin` a las 10:00 AM de hoy:

`echo "{{comando}}" | at 1000`

- Ejecuta comandos desde un archivo determinado el próximo martes:

`at -f {{ruta/al/archivo}} 9:30 PM Tue`

- Lista todos los trabajos en cola para el usuario actual (igual que `atq`):

`at -l`

- Visualiza un trabajo específico:

`at -c {{número_de_trabajo}}`
