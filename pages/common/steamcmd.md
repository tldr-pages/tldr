# steamcmd

> A command-line version of the Steam client.
> More information: <https://manned.org/steamcmd>.

- Install or update an application anonymously:

`steamcmd +login {{anonymous}} +app_update {{app_id}} +quit`

- Install or update an application using the specified credentials:

`steamcmd +login {{username}} +app_update {{app_id}} +quit`

- Define a custom install location:

`steamcmd +force_install_dir {{path/to/directory}} +login {{anonymous}} +app_update {{app_id}} validate +quit`

- Install an application for a specific platform:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{app_id}} validate +quit`

- Run a script file:

`steamcmd +runscript {{script.txt}}`

- Clear cached login credentials for a user:

`steamcmd +login {{username}} +logout +quit`
