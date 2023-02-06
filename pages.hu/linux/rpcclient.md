# rpcclient

> MS-RPC kliens eszköz (a samba csomag része). További információ: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- Csatlakozás egy távoli állomáshoz:

`rpcclient --user {{domain}}\{{username}}%{{password}} {{ip}}`

- Csatlakozás egy távoli állomáshoz egy tartományban jelszó nélkül:

`rpcclient --user {{username}} --workgroup {{domain}} --no-pass {{ip}}`

- Csatlakozás egy távoli állomáshoz a jelszó hash átadásával:

`rpcclient --user {{domain}}\{{username}} --pw-nt-hash {{ip}}`

- Shell parancsok végrehajtása távoli állomáson:

`rpcclient --user {{domain}}\{{username}}%{{password}} --command {{semicolon_separated_commands}} {{ip}}`

- Tartományi felhasználók megjelenítése:

`rpcclient $> enumdomusers`

- Jogosultságok megjelenítése:

`rpcclient $> enumprivs`

- Egy adott felhasználóra vonatkozó információk megjelenítése:

`rpcclient $> queryuser {{username|rid}}`

- Új felhasználó létrehozása a tartományban:

`rpcclient $> createdomuser {{username}}`
