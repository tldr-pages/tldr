# mount.cifs

> Mount SMB (Server Message Block) of CIFS (Common Internet File System) shares.
> Opmerking: u kunt ook hetzelfde doen door de optie `-t cifs` door te geven aan `mount`.
> Meer informatie: <https://manned.org/mount.cifs>.

- Verbinding maken met de opgegeven gebruikersnaam of `$USER` als standaard (U wordt gevraagd om een wachtwoord):

`mount.cifs -o user={{gebruikersnaam}} //{{server}}/{{share_name}} {{mountpoint}}`

- Maak verbinding als gastgebruiker (zonder wachtwoord):

`mount.cifs -o guest //{{server}}/{{share_name}} {{mountpoint}}`

- Stel eigendomsinformatie in voor de mounted map:

`mount.cifs -o uid={{user_id|gebruikersnaam}},gid={{group_id|groupname}} //{{server}}/{{share_name}} {{mountpoint}}`
