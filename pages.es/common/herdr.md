# herdr

> Gestor de espacios de trabajo en terminal para agentes de programación de IA.
> Nota: La estructura es Sesión > Espacio de trabajo > Pestaña > Panel.
> Vea también: `tmux`, `zellij`, `screen`.
> Más información: <https://herdr.dev/docs/cli-reference/>.

- Inicia una nueva sesión o se conecta a la predeterminada:

`herdr`

- Muestra el estado del cliente y del servidor locales:

`herdr status`

- Genera la configuración predeterminada y la muestra en `stdout`:

`herdr --default-config`

- Se desconecta de la sesión actual (dentro de una sesión de herdr):

`<Ctrl b><?>`

- Muestra las combinaciones de teclas (dentro de una sesión de herdr):

`<Ctrl b><?>`

- Crea un nuevo espacio de trabajo (dentro de una sesión de herdr):

`<Ctrl b><Shift n>`

- Crea una nueva pestaña (dentro de una sesión de herdr):

`<Ctrl b><c>`

- Divide el panel vertical u horizontalmente (dentro de una sesión de herdr):

`<Ctrl b>{{<v>|<->}}`
