# lsusb

> Muestra información sobre los buses USB y los dispositivos conectados a ellos.
> Más información: <https://manned.org/lsusb>.

- Muestra todos los dispositivos USB disponibles:

`lsusb`

- Lista la jerarquía USB como un árbol:

`lsusb -t`

- Muestra información detallada sobre los dispositivos USB:

`lsusb --verbose`

- Muestra información detallada sobre un dispositivo USB:

`lsusb --verbose -s {{bus}}:{{número de dispositivo}}`

- Muestra sólo los dispositivos con un ID de proveedor y producto determinados:

`lsusb -d {{vendedor}}:{{producto}}`
