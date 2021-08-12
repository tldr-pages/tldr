# steamcmd

> O versiune de linie de comandă a clientului Steam.
> Mai multe informaţii: <https://manned.org/steamcmd>

- Instalați sau actualizați o aplicație anonim:

`steamcmd +login {{anonymous}} +app_update {{appid}} +quit`

- Instalați sau actualizați o aplicație utilizând acreditările specificate:

`steamcmd +login {{username}} +app_update {{appid}} +quit`

- Instalați o aplicație pentru o anumită platformă:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{appid}} validate +quit`
