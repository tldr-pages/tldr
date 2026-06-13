# crontab

> Programa trabajos recurrentes (cron jobs) para ejecutarse a intervalos de tiempo para el usuario actual.
> Más información: <https://manned.org/crontab>.

- Edita el archivo crontab para el usuario actual:

`crontab -e`

- Edita el archivo crontab para un usuario específico:

`sudo crontab -e -u {{usuario}}`

- Reemplaza el crontab actual con el contenido del archivo dado:

`crontab {{ruta/al/archivo}}`

- Muestra una lista de cron jobs existentes para el usuario actual:

`crontab -l`

- Elimina todos los cron jobs para el usuario actual:

`crontab -r`

- Ejemplo de entrada contrab que ejecuta un comando a las 10:00 cada día (* significa cualquier valor):

`0 10 * * * {{comando_a_ejecutar}}`

- Ejemplo de entrada crontab, que ejecuta un comando cada 10 minutos:

`*/10 * * * * {{comando_a_ejecutar}}`

- Ejemplo de entrada crontab, que ejecuta un script a las 02:30 cada viernes:

`30 2 * * Fri /{{/ruta/a/script.sh}}`
