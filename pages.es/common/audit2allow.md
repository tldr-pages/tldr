# audit2allow

> Crea un módulo de política local SELinux para permitir reglas basadas en operaciones denegadas encontradas en los logs.
> Nota: Utiliza audit2allow con precaución - revisa siempre la directiva generada antes de aplicarla, ya que puede permitir un acceso excesivo.
> Más información: <https://manned.org/audit2allow>.

- Genera una política local para permitir el acceso a todos los servicios denegados:

`sudo audit2allow --all -M {{nombre_de_la_normativa_local}}`

- Genera un módulo de normativa local para conceder acceso a un proceso/servicio/comando específico de los registros de auditoría:

`sudo grep {{apache2}} /var/log/audit/audit.log | sudo audit2allow -M {{nombre_de_la_normativa_local}}`

- Inspecciona y revisa el archivo Type Enforcement (.te) para una normativa local:

`vim {{nombre_de_la_normativa_local}}.te`

- Instala un módulo de normativa local:

`sudo semodule -i {{nombre_de_la_normativa_local}}.pp`
