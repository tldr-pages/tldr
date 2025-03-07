# timew

> Una herramienta de registro y seguimiento de tiempo para medir la duración de actividades.
> Mas información: <https://timewarrior.net/docs>.

- Comenzar a cronometrar una actividad:

`timew start`

- Etiquetar la actividad actual:

`timew tag {{etiqueta_de_la_actividad}}`

- Comenzar a cronometrar y a la vez etiquetar una actividad nueva:

`timew start {{etiqueta_de_la_actividad}}`

- Detener la actividad actual:

`timew stop`

- Registrar una actividad pasada:

`timew track {{tiempo_de_inicio} - {{tiempo_de_finalización}} {{etiqueta_de_la_actividad}}`

- Ver los elementos registrados de hoy:

`timew summary`

- Ve un reporte del último día, semana, mes actual, etc.:

`timew summary :{{today|yesterday|week|lastweek|month|lastmonth|year|lastyear}}`
