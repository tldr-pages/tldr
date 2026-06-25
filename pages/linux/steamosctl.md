# steamosctl

> Control the SteamOS system.
> More information: <https://gitlab.com/evlaV/steamos-manager>.

- Change to desktop mode:

`steamosctl switch-to-desktop-mode`

- Change to gamemode:

`steamosctl switch-to-game-mode`

- Change whether the system opens gamemode or desktop during login:

`steamosctl set-default-login-mode {{game|desktop}}`

- Get currently used CPU scheduler:

`steamosctl get-cpu-scheduler`

- Set the system to use a specific CPU scheduler:

`steamosctl set-cpu-scheduler {{none|lavd|...}}`

- Display available desktop sessions:

`steamosctl get-valid-desktop-sessions`

- Set the the default desktop session:

`steamosctl set-default-desktop-session {{plasma.desktop|plasmax11.desktop|...}}`

- Display help:

`steamosctl`
