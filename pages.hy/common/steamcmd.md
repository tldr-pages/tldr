# steamcmd

> Steam հաճախորդի հրամանի տող տարբերակ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/steamcmd>:.

- Տեղադրեք կամ թարմացրեք հավելվածը անանուն.:

`steamcmd +login {{anonymous}} +app_update {{app_id}} +quit`

- Տեղադրեք կամ թարմացրեք հավելված՝ օգտագործելով նշված հավատարմագրերը.:

`steamcmd +login {{username}} +app_update {{app_id}} +quit`

- Սահմանեք հատուկ տեղադրման վայրը.:

`steamcmd +force_install_dir {{path/to/directory}} +login {{anonymous}} +app_update {{app_id}} validate +quit`

- Տեղադրեք հավելված հատուկ հարթակի համար.:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{anonymous}} +app_update {{app_id}} validate +quit`

- Գործարկել սցենարի ֆայլը.:

`steamcmd +runscript {{script.txt}}`

- Մաքրել քեշավորված մուտքի հավատարմագրերը օգտվողի համար.:

`steamcmd +login {{username}} +logout +quit`
