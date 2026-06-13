# aa-status

> Lista los módulos AppArmor cargados actualmente.
> Vea también: `aa-complain`, `aa-disable`, `aa-enforce`.
> Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Muestra el estado:

`sudo aa-status`

- Muestra el número de políticas cargadas:

`sudo aa-status --profiled`

- Muestra el número de políticas impuestas cargadas:

`sudo aa-status --enforced`

- Muestra el número de políticas no obligatorias cargadas:

`sudo aa-status --complaining`

- Muestra el número de políticas impuestas cargadas que terminan tareas:

`sudo aa-status --kill`
