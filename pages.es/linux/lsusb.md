# lsusb

> Muestra información sobre puertos y dispositivos USB.

- Lista todos los dispositivos USB disponibles:

`lsusb`

- Lista la jerarquía de dispositivos USB en forma de árbol:

`lsusb -t`

- Lista los dispositivos USB de forma verbosa:

`lsusb --verbose`

- Lista información detallada acerca de un dispositivo USB determinado:

`lsusb -D {{dispositivo}}`

- Lista solo dispositivos con un ID de ensamblador y producto determinado:

`lsusb -d {{ensamblador}}:{{producto}}`
