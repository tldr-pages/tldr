# timew

> Una herramienta de registro y seguimiento de tiempo para medir la duración de actividades.
> Más información: <https://timewarrior.net/docs>.

- Comienza a cronometrar una actividad:

`timew start`

- Etiqueta la actividad actual:

`timew tag {{etiqueta_de_la_actividad}}`

- Comienza a cronometrar y a la vez etiquetar una actividad nueva:

`timew start {{etiqueta_de_la_actividad}}`

- Detiene la actividad actual:

`timew stop`

- Registra una actividad pasada:

`timew track {{tiempo_de_inicio}} - {{tiempo_de_finalización}} {{etiqueta_de_la_actividad}}`

- Ve los elementos registrados de hoy:

`timew summary`

- Ve un reporte del último día, semana, mes actual, etc.:

`timew summary :{{today|yesterday|week|lastweek|month|lastmonth|year|lastyear}}`
