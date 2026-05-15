# iw dev

> Muestra y gestiona dispositivos inalámbricos.
> Para obtener una lista de canales, frecuencias e información de registro: <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
> Más información: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Configura el dispositivo en modo monitor (la interfaz debe estar inactiva primero. Vea también: `ip link`):

`sudo iw dev {{wlanX}} set type monitor`

- Configura el dispositivo en modo gestionado (la interfaz debe estar inactiva primero):

`sudo iw dev {{wlanX}} set type managed`

- Configura el canal Wi-Fi del dispositivo (el dispositivo debe estar primero en modo monitor con la interfaz activa):

`sudo iw dev {{wlanX}} set channel {{nombre_canal}}`

- Configura la frecuencia Wi-Fi del dispositivo en MHz (el dispositivo debe estar primero en modo monitor con la interfaz activa):

`sudo iw dev {{wlanX}} set freq {{frec_en_mhz}}`

- Muestra toda la información de las estaciones conocidas:

`iw dev {{wlanX}} station dump`

- Crea una interfaz virtual en modo monitor con una dirección MAC específica:

`sudo iw dev {{wlanX}} interface add "{{nombre_vif}" type monitor addr {{12:34:56:aa:bb:cc}}`

- Elimina la interfaz virtual:

`sudo iw dev "{{nombre_vif}}" del`
