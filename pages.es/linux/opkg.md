# opkg

> Un gestor de paquetes ligero utilizado para instalar paquetes OpenWrt.
> Más información: <https://openwrt.org/docs/guide-user/additional-software/opkg>.

- Instala un paquete:

`opkg install {{paquete}}`

- Elimina un paquete:

`opkg remove {{paquete}}`

- Actualiza la lista de paquetes disponibles:

`opkg update`

- Actualiza uno o varios paquetes específicos:

`opkg upgrade {{paquete(s)}}`

- Muestra información sobre un paquete concreto:

`opkg info {{paquete}}`

- Lista todos los paquetes disponibles:

`opkg list`

- Averigua a qué paquete pertenece un archivo:

`opkg search {{ruta/al/archivo}}`

- Lista todos los archivos de un paquete:

`opkg files {{paquete}}`
