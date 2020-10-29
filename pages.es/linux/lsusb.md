# lsusb

> Muestra información sobre puertos y dispositivos USB

- Lista todos los dispositivos USB disponibles:

`lsusb`

- Lista la jerarquía de dispositivos USB en forma de arbol

`lsusb -t`

- Lista los dispositivos USB de forma verbosa:

`lsusb --verbose`

- Lista información destallada acerca de un dispositivo USB en especifico:

`lsusb -D {{dispositivo}}`

- Lista solo dispositivos con un ID de ensamblador y producto en especifico:

`lsusb -d {{ensamblador}}:{{producto}}`
