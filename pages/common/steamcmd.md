# steamcmd

> A command-line version of the Steam client.
> More information: <https://manned.org/steamcmd>.

- Install or update an application anonymously:

`steamcmd +login {{anonymous}} +app_update {{appid}} +quit`

- Install or update an application using the specified credentials:

`steamcmd +login {{username}} {{password}} +app_update {{appid}} +quit`

- Install an application for a specific platform such as Windows:

`steamcmd +@sSteamCmdForcePlatformType {{platform}} +login {{anonymous}} +app_update {{appid}} validate +quit`
