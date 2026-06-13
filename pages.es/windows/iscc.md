# iscc

> Compilador para instaladores de Inno Setup.
> Compila scripts de Inno Setup en un ejecutable de instalador de Windows.
> Más información: <https://jrsoftware.org/isinfo.php>.

- Compila un script de Inno Setup:

`iscc {{ruta\al\archivo.iss}}`

- Compila un instalador de Inno Setup de forma silenciosa:

`iscc /Q {{ruta\al\archivo.iss}}`

- Compila un instalador de Inno Setup firmado:

`iscc /S={{nombre}}={{comando}} {{ruta\al\archivo.iss}}`
