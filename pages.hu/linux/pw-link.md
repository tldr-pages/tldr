# pw-link

> A portok közötti kapcsolatok kezelése a PipeWire-ben. További információ: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Az összes audió kimeneti és bemeneti port listázása:

`pw-link --output --input`

- Létrehoz egy kapcsolatot egy kimeneti és egy bemeneti port között:

`pw-link {{output_port_name}} {{input_port_name}}`

- Két port összekapcsolása:

`pw-link --disconnect {{output_port_name}} {{input_port_name}}`

- Súgó megjelenítése:

`pw-link -h`
