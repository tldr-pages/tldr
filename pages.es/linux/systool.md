# systool

> Vea información de dispositivos del sistema por bus y clases.
> Este comando es parte del paquete `sysfs`.
> Más información: <https://manned.org/systool>.

- Lista todos los atributos de los dispositivos de un bus (ej. `pci`, `usb`). Vea todos los buses usando `ls /sys/bus`:

`systool -b {{bus}} -v`

- Lista todos los atributos de una clase de dispositivos (ej. `drm`, `block`). Vea todas las clases usando `ls /sys/class`:

`systool -c {{clase}} -v`

- Muestra solo los controladores de un bus (ej. `pci`, `usb`):

`systool -b {{bus}} -D`
