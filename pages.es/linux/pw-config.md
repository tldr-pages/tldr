# pw-config

> Enumera las rutas y secciones de configuración que utilizarán el servidor y los clientes de PipeWire.
> Más información: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- Lista todos los archivos de configuración que se utilizarán:

`pw-config`

- Lista todos los archivos de configuración que utilizará el servidor PulseAudio de PipeWire:

`pw-config --name pipewire-pulse.conf`

- Lista todas las secciones de configuración utilizadas por el servidor PulseAudio de PipeWire:

`pw-config --name pipewire-pulse.conf list`

- Lista los fragmentos `context.properties` utilizados por los clientes JACK:

`pw-config --name jack.conf list context.properties`

- Lista las `context.properties` fusionadas utilizadas por los clientes JACK:

`pw-config --name jack.conf merge context.properties`

- Lista los `context.modules` fusionados utilizados por el servidor PipeWire y [r]eformat:

`pw-config --name pipewire.conf --recurse merge context.modules`

- Muestra la ayuda:

`pw-config --help`
