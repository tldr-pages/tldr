# iwlist

> Obtén información detallada de una interfaz inalámbrica.
> Más información: <https://manned.org/iwlist.8>.

- Muestra la lista de puntos de acceso y células ad-hoc en alcance:

`iwlist {{interfaz_inalámbrica}} scan`

- Muestra las frecuencias disponibles en el dispositivo:

`iwlist {{interfaz_inalámbrica}} frequency`

- Lista las tasas de bits soportadas por el dispositivo:

`iwlist {{interfaz_inalámbrica}} rate`

- Enumera los parámetros de autenticación WPA configurados actualmente:

`iwlist {{interfaz_inalámbrica}} auth`

- Enumera todas las claves de cifrado WPA configuradas en el dispositivo:

`iwlist {{interfaz_inalámbrica}} wpakeys`

- Enumera los tamaños de clave de cifrado admitidos y todas las claves de cifrado configuradas en el dispositivo:

`iwlist {{interfaz_inalámbrica}} keys`

- Enumera los distintos atributos y modos de gestión de energía del dispositivo:

`iwlist {{interfaz_inalámbrica}} power`

- Enumera los elementos de información genéricos configurados en el dispositivo (utilizados para la compatibilidad con WPA):

`iwlist {{interfaz_inalámbrica}} genie`
