# protontricks

> A simple wrapper that runs Winetricks commands for Proton enabled games.
> More information: <https://github.com/Matoking/protontricks>.

- Run the protontricks GUI:

`protontricks --gui`

- Run Winetricks for a specific game:

`protontricks {{appid}} {{winetricks_args}}`

- Run a command within a game's installation directory:

`protontricks -c {{command}} {{appid}}`

- [l]ist all installed games:

`protontricks -l`

- [s]earch for a game's App ID by name:

`protontricks -s {{game_name}}`

- Display help:

`protontricks --help`
