# protontricks

> A simple wrapper that runs Winetricks commands for Proton enabled games.
> More information: <https://github.com/Matoking/protontricks#usage>.

- Run the protontricks GUI:

`protontricks --gui`

- Run Winetricks for a specific game:

`protontricks {{appid}} {{winetricks_args}}`

- Run a command within a game's installation directory:

`protontricks {{[-c|--command]}} {{command}} {{appid}}`

- List all installed games:

`protontricks {{[-l|--list]}}`

- Search for a game's App ID by name:

`protontricks {{[-s|--search]}} {{game_name}}`

- Run an executable in the proton environment of a specific game:

`protontricks-launch --appid {{appid}} {{path/to/executable.exe}}`

- Display help:

`protontricks {{[-h|--help]}}`
