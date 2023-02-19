# abroot

> La utilidad ABRoot proporciona inmutabilidad y atomicidad completas al realizar transacciones entre 2 estados de partición raíz (A⟺B).
> También permite transacciones bajo demanda a través de un shell transaccional.
> Más información: <https://github.com/Vanilla-OS/ABRoot>.

- Muestra el estado actual o futuro de la partición raíz:

`sudo abroot get {{present|future}}`

- Ingrese el shell transaccional en la partición raíz futura y cambie la raíz en el próximo arranque:

`sudo abroot shell`

- Ejecute un comando específico en el shell transaccional en la futura partición raíz y cambie a él en el siguiente arranque:

`sudo abroot exec "{{comando}}"`

- Instale paquetes específicos en el host dentro del shell transaccional en la partición raíz futura y cambie a él en el próximo arranque:

`sudo abroot exec apt install {{paquete1 paquete2 ...}}`

- Actualice la partición de arranque (solo para usuarios avanzados):

`sudo abroot _update-boot`

- Mostrar ayuda:

`abroot --help`

- Mostrar version:

`abroot --version`
