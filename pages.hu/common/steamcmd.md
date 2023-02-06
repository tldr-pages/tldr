# steamcmd

> A Steam kliens parancssori változata. További információ: <https://manned.org/steamcmd>.

- Alkalmazás névtelen telepítése vagy frissítése:

`steamcmd +login {{anonymous}} +app_update {{appid}} +quit`

- Alkalmazás telepítése vagy frissítése a megadott hitelesítő adatokkal:

`steamcmd +login {{username}} +app_update {{appid}} +quit`

- Alkalmazás telepítése egy adott platformra:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{appid}} validate +quit`
