# ansiweather

> Un script de shell para mostrar las condiciones meteorológicas actuales en tu terminal.
> Más información: <https://github.com/fcambus/ansiweather>.

- Muestra una previsión usando unidades métricas de los siguientes siete días de una ubicación:

`ansiweather -u metric -f 7 -l {{Rzeszow,PL}}`

- Muestra una previsión de los siguientes cinco días con símbolos e información de luz diurna de tu ubicación actual:

`ansiweather -F -s true -d true`

- Muestra una previsión con los datos de viento y humedad de tu ubicación actual:

`ansiweather -w true -h true`
