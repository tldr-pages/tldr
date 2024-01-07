# ansiweather

> Un script de shell para mostrar las condiciones meteorológicas actuales en tu terminal.
> Más información: <https://github.com/fcambus/ansiweather>.

- Muestra una previsión en unidades métricas para los próximos cinco días en Rzeszow, Polonia:

`ansiweather -u {{metric}} -f {{5}} -l {{Rzeszow,PL}}`

- Muestra una previsión con símbolos y datos de la luz del día dada tu ubicación actual:

`ansiweather -s {{true}} -d {{true}}`

- Muestra una previsión con los datos de viento y humedad dada tu ubicación actual:

`ansiweather -w {{true}} -h {{true}}`
