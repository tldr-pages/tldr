# btrfs scrub

> Realiza un scrub en sistemas de archivos btrfs para verificar la integridad de los datos.
> Se recomienda ejecutar un scrub una vez al mes.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Inicia un scrub:

`sudo btrfs scrub start {{ruta/al_montaje_btrfs}}`

- Muestra el estado de un scrub en curso o del último completado:

`sudo btrfs scrub status {{ruta/al_montaje_btrfs}}`

- Cancela un scrub en curso:

`sudo btrfs scrub cancel {{ruta/al_montaje_btrfs}}`

- Reanuda un scrub previamente cancelado:

`sudo btrfs scrub resume {{ruta/al_montaje_btrfs}}`

- Inicia un scrub, pero espera a que termine antes de salir:

`sudo btrfs scrub start -B {{ruta/al_montaje_btrfs}}`

- Inicia un scrub en modo silencioso (no imprime errores ni estadísticas):

`sudo btrfs scrub start -q {{ruta/al_montaje_btrfs}}`
