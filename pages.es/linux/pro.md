# pro

> Administra los servicios de Ubuntu Pro.
> Más información: <https://manned.org/ubuntu-advantage.1>.

- Conecta tu sistema al contrato de soporte de Ubuntu Pro:

`sudo pro attach`

- Muestra el estado de los servicios de Ubuntu Pro:

`pro status`

- Chequea si el sistema está afectado por una vulnerabilidad específica (y aplica la corrección si es posible):

`pro fix {{CVE-number}}`

- Muestra el número de paquetes no soportados:

`pro security-status`

- Lista paquetes que ya no están disponibles para descargar:

`pro security-status --unavailable`

- Lista los paquetes de terceros:

`pro security-status --thirdparty`
