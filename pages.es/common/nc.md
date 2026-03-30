# nc

> Redirige E/S hacia un flujo de red mediante esta versátil herramienta.
> Más información: <https://manned.org/nc>.

- Inicia un [l]istener en el [p]uerto TCP especificado y envía un archivo hacia él:

`nc < {{nombre_archivo}} -l -p {{puerto}}`

- Se conecta a un listener destino en el puerto especificado y recibe un archivo de él:

`nc {{host}} {{puerto}} > {{nombre_archivo_recibido}}`

- Escanea los puertos TCP abiertos de un host específico:

`nc -v -z -w {{tiempo_espera_segundos}} {{host}} {{puerto_inicio}}-{{puerto_fin}}`

- Inicia un [l]istener en el [p]uerto TCP especificado y da acceso al shell local a la parte conectada (esto es peligroso y puede ser abusado):

`nc -l -p {{puerto}} -e {{ejecutable_shell}}`

- Se conecta a un listener destino y da acceso al shell local a la parte remota (esto es peligroso y puede ser abusado):

`nc {{host}} {{puerto}} -e {{ejecutable_shell}}`
