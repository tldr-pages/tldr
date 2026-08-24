# btrfs scrub

> Realiza un scrub en sistemas de archivos btrfs para verificar la integridad de los datos.
> Se recomienda ejecutar un scrub una vez al mes.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Inicia un scrub:

`sudo btrfs {{[sc|scrub]}} start {{ruta/al_montaje_btrfs}}`

- Muestra el estado de un scrub en curso o del último completado:

`sudo btrfs {{[sc|scrub]}} status {{ruta/al_montaje_btrfs}}`

- Cancela un scrub en curso:

`sudo btrfs {{[sc|scrub]}} {{[c|cancel]}} {{ruta/al_montaje_btrfs}}`

- Reanuda un scrub previamente cancelado:

`sudo btrfs {{[sc|scrub]}} {{[r|resume]}} {{ruta/al_montaje_btrfs}}`

- Inicia un scrub, pero espera a que termine antes de salir:

`sudo btrfs {{[sc|scrub]}} start -B {{ruta/al_montaje_btrfs}}`

- Inicia un scrub en modo silencioso (no imprime errores ni estadísticas):

`sudo btrfs {{[sc|scrub]}} start {{[-q|--quiet]}} {{ruta/al_montaje_btrfs}}`
