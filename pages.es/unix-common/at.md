# at

> Ejecuta comandos una vez en un momento posterior.
> El servicio atd (o atrun) debe estar ejecutándose para las ejecuciones reales.
> Más información: <https://manned.org/at>.

- Ejecuta comandos desde la entrada estándar en 5 minutos (pulsa `Ctrl + D` cuando termines):

`at now + 5 minutes`

- Ejecuta un comando desde la entrada estándar a las 10:00 AM de hoy:

`echo "{{./make_db_backup.sh}}" | at 1000`

- Ejecuta comandos desde un archivo dado el próximo martes:

`at -f {{ruta/al/archivo}} 9:30 PM Tue`
