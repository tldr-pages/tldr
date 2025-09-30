# update-alternatives

> Mantiene convenientemente enlaces simbólicos para determinar los comandos predeterminados.
> Más información: <https://manned.org/update-alternatives>.

- Agrega un enlace simbólico:

`sudo update-alternatives --install {{ruta/al/enlace_simbólico}} {{comando}} {{ruta/al/comando}} {{prioridad}}`

- Configura un enlace simbólico para 'java':

`sudo update-alternatives --config {{java}}`

- Quita un enlace simbólico:

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- Muestra información sobre un comando específico:

`update-alternatives --display {{java}}`

- Muestra todos los comandos y su selección actual:

`update-alternatives --get-selections`
