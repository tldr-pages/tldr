# pactrans

> Instala, elimina y actualiza paquetes ALPM.
> Vea también: `pacinstall`, `pacremove`.
> Más información: <https://github.com/andrewgregory/pacutils/blob/master/doc/pactrans.pod>.

- Instala un paquete desde un repositorio:

`sudo pactrans --install {{nombre_del_paquete}}`

- Elimina un paquete:

`sudo pactrans --remove {{nombre_del_paquete}}`

- Actualiza todos los paquetes instalados:

`sudo pactrans --sysupgrade`

- Instala un archivo de paquete:

`sudo pactrans --file {{ruta/al/paquete.pkg.tar.zst}}`

- Reemplaza un paquete instalado localmente por uno de un repositorio:

`sudo pactrans local/{{nombre_del_paquete_a_eliminar}} {{nombre_del_repositorio}}/{{nombre_del_paquete_a_instalar}}`

- Muestra lo que haría la transacción sin ejecutarla:

`pactrans --print-only --install {{nombre_del_paquete}}`
