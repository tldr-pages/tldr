# par2

> Verificación y reparación de archivos utilizando archivos de paridad compatibles con PAR 2.0 (archivos .par2).
> Más información: <https://github.com/Parchive/par2cmdline/>.

- Crea un archivo de paridad con un nivel de porcentaje de redundancia establecido:

`par2 create -r{{1..100}} -- {{ruta/al/archivo}}`

- Crea un archivo de paridad con un número determinado de archivos de volumen (además del archivo de índice):

`par2 create -n{{1..32768}} -- {{ruta/al/archivo}}`

- Verifica un fichero con un archivo de paridad:

`par2 verify -- {{ruta/al/archivo.par2}}`

- Repara un fichero con un archivo de paridad:

`par2 repair -- {{ruta/al/archivo.par2}}`
