# tex-fmt

> Formatea el código fuente LaTeX.
> Más información: <https://github.com/WGUNDERWOOD/tex-fmt>.

- Formatea un archivo, sobrescribiendo el original:

`tex-fmt {{ruta/al/archivo.tex}}`

- Comprueba si un archivo está formateado correctamente:

`tex-fmt --check {{ruta/al/archivo.tex}}`

- Formatea un archivo leído de `stdin` y lo imprime en `stdout`:

`cat {{ruta/al/archivo.tex}} | tex-fmt --stdin`
