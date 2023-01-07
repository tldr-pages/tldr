# steamcmd

> Ein Kommandozeilenwerkzeug, um über Steam verfügbare Anwendungen zu verwalten.
> Weitere Informationen: <https://manned.org/steamcmd>.

- Installiere und aktualisiere eine Anwendung ohne dich einzuloggen:

`steamcmd +login {{anonymous}} +app_update {{anwendungs_id}} +quit`

- Installiere oder aktualisiere eine Anwendung unter Angabe deiner Zugangsdaten:

`steamcmd +login {{benutzername}} +app_update {{anwendungs_id}} +quit`

- Installiere eine Anwendung für eine bestimmte Plattform:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{benutzername}} +app_update {{anwendungs_id}} validate +quit`
