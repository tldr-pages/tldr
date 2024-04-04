# Gammastep

> Ajusta la temperatura del color de la pantalla según la hora del día.
> Más información: <https://gitlab.com/chinstrap/gammastep>.

- Activa Gammastep con una [t]emperatura específica durante el día (por ejemplo, 5700k) y por la noche (por ejemplo, 3600k):

`gammastep -t {{5700}}:{{3600}}`

- Activa Gammastep con una [l]ocación personalizada especificada manualmente:

`gammastep -l {{latitud}}:{{longitud}}`

- Activa Gammastep con un [b]rillo de pantalla específico durante el día (por ejemplo, 70%) y la noche (por ejemplo, 40%), con un brillo mínimo del 10% y uno máximo del 100%:

`gammastep -b {{0.7}}:{{0.4}}`

- Activa Gammastep con niveles de [g]ama personalizados (entre 0 y 1):

`gammastep -g {{rojo}}:{{verde}}:{{azul}}`

- Activa Gammastep con una temperatura de color c[O]nstante e invariable:

`gammastep -O {{temperatura}}`

- Restablece los ajustes de temperatura aplicados por Gammastep:

`gammastep -x`
