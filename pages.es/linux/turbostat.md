# turbostat

> Informa de la topología del procesador, frecuencia, temperatura, potencia y estadísticas de inactividad.
> Más información: <https://manned.org/turbostat.8>.

- Muestra las estadísticas cada cinco segundos:

`sudo turbostat`

- Muestra las estadísticas cada cierto número de segundos:

`sudo turbostat -i {{n_segundos}}`

- Muestra información sin decodificar ni imprimir la cabecera de configuración del sistema:

`sudo turbostat --quiet`

- Muestra información útil sobre el CPU cada segundo, sin información de cabecera:

`sudo turbostat --quiet --interval 1 --cpu 0-{{cuenta_hilos_CPU}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- Muestra ayuda:

`turbostat --help`
