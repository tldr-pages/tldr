# kodi-send

> Send actions to Kodi.
> More information: <https://kodi.wiki/view/List_of_built-in_functions>.

- Send a navigation event:

`kodi-send {{[-a|--action]}} {{Up|Down|Left|Right|Select|Back|ContextMenu|...}}`

- Activate a specific window:

`kodi-send {{[-a|--action]}} "ActivateWindow({{Home|Videos|Settings|...}})"`

- Control the media player:

`kodi-send {{[-a|--action]}} "PlayerControl({{Play|Stop|Forward|Rewind|...)"`

- Send keyboard key presses:

`kodi-send --button {{key1}} --button {{key2}} --button {{...}}`

- Quit Kodi:

`kodi-send {{[-a|--action]}} Quit`

- Reboot the system:

`kodi-send {{[-a|--action]}} Reboot`

- Send an action to a remote host:

`kodi-send --host {{192.168.0.1}} --port {{9777}} {{[-a|--action]}} {{Quit}}`

- Display help:

`kodi-send {{[-?|--help]}}`
