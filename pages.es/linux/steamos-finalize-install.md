# steamos-finalize-install

> Finaliza la instalación de SteamOS configurando los cargadores de arranque y aplicando las actualizaciones del sistema.
> Más información: <https://gitlab.com/users/evlaV/projects>.

- Finaliza la instalación:

`sudo steamos-finalize-install`

- Finaliza sin actualizar los cargadores de arranque ni el núcleo:

`sudo steamos-finalize-install --no-bootloaders --no-kernel`

- Omite todos los pasos de migración:

`sudo steamos-finalize-install --no-migrate`

- Establece un hash de raíz específico durante la finalización:

`sudo steamos-finalize-install --roothash {{hash}}`

- Fuerza los pasos de migración del sistema independientemente del entorno:

`sudo steamos-finalize-install --force`
