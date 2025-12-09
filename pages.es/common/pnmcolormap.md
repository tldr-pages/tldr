# pnmcolormap

> Crea mapa de colores cuantizado para una imagen PNM.
> Más información: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- Genera una imagen usando sólo 'n_colores' o menos colores lo más cerca posible de la imagen de entrada:

`pnmcolormap {{n_colores}} {{ruta/a/la/entrada.pnm}} > {{ruta/al/resultado.ppm}}`

- Utiliza la estrategia de splitspread para determinar los colores de salida, posiblemente produciendo un mejor resultado para imágenes con detalles pequeños:

`pnmcolormap -splitspread {{n_colores}} {{ruta/a/la/entrada.pnm}} > {{ruta/al/resultado.ppm}}`

- Ordena el mapa de colores resultante, que es útil para comparar los mapas de colores:

`pnmcolormap -sort {{ruta/a/la/entrada.pnm}} > {{ruta/al/resultado.ppm}}`
