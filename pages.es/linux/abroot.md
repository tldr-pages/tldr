# abroot

> La utilidad ABRoot proporciona inmutabilidad y atomicidad completas al realizar transacciones entre 2 estados de partición raíz (A⟺B).
> También permite transacciones bajo demanda a través de un shell transaccional.
> Más información: <https://github.com/Vanilla-OS/ABRoot>.

- Muestra el estado actual o futuro de la partición raíz:

`sudo abroot get {{present|future}}`

- Ingresa el shell transaccional en la partición raíz futura y cambia la raíz en el próximo arranque:

`sudo abroot shell`

- Ejecuta un comando específico en el shell transaccional en la futura partición raíz y cambia a él en el siguiente arranque:

`sudo abroot exec "{{comando}}"`

- Instala paquetes específicos en el host dentro del shell transaccional en la partición raíz futura y cambia a él en el próximo arranque:

`sudo abroot exec apt install {{paquete1 paquete2 ...}}`

- Actualiza la partición de arranque (solo para usuarios avanzados):

`sudo abroot _update-boot`

- Muestra la ayuda:

`abroot --help`

- Muestra la version:

`abroot --version`
