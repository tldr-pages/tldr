# dot_clean

> Fusiona los archivos ._* con los archivos nativos correspondientes.
> Más información: <https://ss64.com/osx/dot_clean.html>.

- Fusiona todos los ficheros `._*` recursivamente:

`dot_clean {{ruta/al/directorio}}`

- Fusiona todos los `._*` en un directorio sin leer subdirectorios (fusión plana):

`dot_clean -f {{ruta/al/directorio}}`

- Fusiona y elimina todos los archivos `._*`:

`dot_clean -m {{ruta/al/directorio}}`

- Elimina sólo los archivos `._*` si hay un archivo nativo coincidente:

`dot_clean -n {{ruta/al/directorio}}`

- Sigue los enlaces simbólicos:

`dot_clean -s {{ruta/al/directorio}}`

- Muestra resultados detallados:

`dot_clean -v {{ruta/al/directorio}}`
