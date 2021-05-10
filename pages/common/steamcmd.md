# steamcmd

> A command-line version of the Steam client.
> More information: <https://manned.org/steamcmd>.

- Install or update an application anonymously:

`steamcmd +login {{anonymous}} +app_update {{appid}} +quit`

- Install or update an application using the specified credentials:

`steamcmd +login {{username}} +app_update {{appid}} +quit`

- Install an application for a specific platform:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{appid}} validate +quit`
