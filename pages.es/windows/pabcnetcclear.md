# pabcnetcclear

> Preprocesar y compilar archivos fuente de PascalABC.NET.
> Más información: <https://pascalabc.net>.

- Compilar el archivo fuente especificado en un ejecutable con el mismo nombre:

`pabcnetcclear {{ruta\al\archivo_fuente.pas}}`

- Compilar el archivo fuente especificado en un ejecutable con el nombre especificado:

`pabcnetcclear /Output:{{ruta\al\_archivo.exe}} {{ruta\al\archivo_fuente.pas}}`

- Compilar el archivo fuente especificado en un ejecutable con el mismo nombre junto con/sin información de depuración:

`pabcnetcclear /Debug:{{0|1}} {{ruta\al\archivo_fuente.pas}}`

- Permitir que las unidades se busquen en la ruta especificada mientras se compila el archivo fuente en un ejecutable con el mismo nombre:

`pabcnetcclear /SearchDir:{{ruta\al\directorio}} {{ruta\al\archivo_fuente.pas}}`

- Compilar el archivo fuente especificado en un ejecutable, definiendo un símbolo:

`pabcnetcclear /Define:{{símbolo}} {{ruta\al\archivo_fuente.pas}}`
