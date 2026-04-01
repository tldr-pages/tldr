# steam

> Video game platform by Valve.
> More information: <https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- Launch Steam, printing debug messages to `stdout`:

`steam`

- Launch Steam and enable its in-app debug console tab:

`steam -console`

- Launch Steam without opening the GUI:

`steam -silent`

- Enable and open the Steam console tab in a running Steam instance:

`steam steam://open/console`

- Log into Steam with the specified credentials:

`steam -login {{username}} {{password}}`

- Launch Steam in Big Picture Mode:

`steam -tenfoot`

- Open a controller configuration:

`steam steam://controllerconfig/{{game_id}}/{{configuration_id}}`

- Exit Steam:

`steam -shutdown`
