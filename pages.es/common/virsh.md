# virsh

> Gestiona dominios invitados `virsh`. (Nota: `guest_id` puede ser el ID, nombre o UUID del invitado).
> Algunos subcomandos como `list` tienen su propia documentación de uso.
> Más información: <https://libvirt.org/manpages/virsh.html>.

- Se conecta a una sesión de hipervisor:

`virsh connect {{qemu:///system}}`

- Activa una red llamada `default`:

`sudo virsh net-start {{default}}`

- Lista todos los dominios:

`virsh list --all`

- Crea un invitado a partir de un archivo de configuración:

`virsh create {{ruta/a/archivo_de_configuración.xml}}`

- Edita el archivo de configuración de un invitado (el editor puede cambiarse con $EDITOR):

`virsh edit {{invitado_id}}`

- Arranca/rearranca/apaga/suspende/reanuda un invitado:

`virsh {{comando}} {{invitado_id}}`

- Guarda el estado actual de un invitado en un archivo:

`virsh save {{invitado_id}} {{nombre_archivo}}`

- Elimina un invitado activo:

`virsh destroy {{invitado_id}} && virsh undefine {{invitado_id}}`
