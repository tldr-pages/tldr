# findstr

> Busca texto especificado dentro de uno o más archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>.

- Busca una o más cadenas en todos los archivos:

`findstr "{{cadena1 cadena2 ...}}" *`

- Busca una o más cadenas en la salida de un comando canalizado:

`{{dir}} | findstr "{{cadena1 cadena2 ...}}"`

- Busca una o más cadenas en todos los archivos de forma recursiva:

`findstr /s "{{cadena1 cadena2 ...}}" *`

- Busca cadenas utilizando una búsqueda sin distinguir entre mayúsculas y minúsculas:

`findstr /i "{{cadena1 cadena2 ...}}" *`

- Busca cadenas en todos los archivos utilizando expresiones regulares:

`findstr /r "{{expresión}}" *`

- Busca una cadena literal (que contenga espacios) en todos los archivos de texto:

`findstr /c:"{{cadena1 cadena2 ...}}" *.txt`

- Muestra el número de línea antes de cada línea coincidente:

`findstr /n "{{cadena1 cadena2 ...}}" *`

- Muestra solo los nombres de archivo que contienen una coincidencia:

`findstr /m "{{cadena1 cadena2 ...}}" *`
