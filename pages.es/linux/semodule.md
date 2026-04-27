# semodule

> Gestiona los módulos de políticas de SELinux.
> Vea también: `audit2allow`, `semanage`.
> Más información: <https://manned.org/semodule>.

- Muestra todos los módulos de políticas instalados:

`sudo semodule {{[-l|--list]}}`

- Instala un nuevo módulo de políticas:

`sudo semodule {{[-i|--install]}} {{ruta/al/módulo.pp}}`

- Elimina un módulo de políticas:

`sudo semodule {{[-r|--remove]}} {{nombre_del_módulo}}`

- Habilita un módulo de políticas:

`sudo semodule {{[-e|--enable]}} {{nombre_del_módulo}}`

- Deshabilita un módulo de políticas:

`sudo semodule {{[-d|--disable]}} {{nombre_del_módulo}}`

- Recarga todos los módulos de políticas:

`sudo semodule {{[-R|--reload]}}`

- Muestra la versión de los módulos de políticas instalados:

`sudo semodule {{[-l|--list]}} {{[-v|--verbose]}}`
