# fpsync

> Ejecuta varios procesos de sincronización localmente o en varios trabajadores remotos a través de SSH.
> Más información: <https://manned.org/fpsync>.

- Sincroniza recursivamente un directorio a otra ubicación:

`fpsync -v {{/ruta/a/origen/}} {{/ruta/a/destino/}}`

- Sincroniza recursivamente un directorio con la última pasada (activa la opción `--delete` de rsync con cada trabajo de sincronización):

`fpsync -v -E {{/ruta/a/origen/}} {{/ruta/a/destino/}}`

- Sincroniza recursivamente un directorio a un destino utilizando 8 trabajos de sincronización simultáneos:

`fpsync -v -n 8 -E {{/ruta/a/origen/}} {{/ruta/a/destino/}}`

- Sincroniza recursivamente un directorio a un destino utilizando 8 trabajos de sincronización concurrentes repartidos entre dos trabajadores remotos (máquina1 y máquina2):

`fpsync -v -n 8 -E -w login@machine1 -w login@machine2 -d {{/ruta/a/directorio/compartido}} {{/ruta/a/origen/}} {{/ruta/a/destino/}}`

- Sincroniza recursivamente un directorio a un destino utilizando cuatro trabajadores locales, cada uno transfiriendo como máximo 1000 archivos y 100 MB por trabajo de sincronización:

`fpsync -v -n 4 -f 1000 -s $((100 * 1024 * 1024)) {{/ruta/a/origen/}} {{/ruta/a/destino/}}`

- Sincroniza de forma recursiva cualquier directorio pero excluye archivos `.snapshot*` específicos (Nota: las opciones y los valores deben estar separados por un carácter de tubería):

`fpsync -v -O "-x|.snapshot*" {{/ruta/a/origen/}} {{/ruta/a/destino/}}`
