# mount.cifs

> Mount SMB (Server Message Block) of CIFS (Common Internet File System) shares.
> Let op: u kunt ook hetzelfde doen door de optie `-t cifs` door te geven aan `mount`.
> Meer informatie: <https://manned.org/mount.cifs>.

- Verbinding maken met de opgegeven gebruikersnaam of `$USER` als standaard (U wordt gevraagd om een wachtwoord):

`mount.cifs -o user={{gebruikersnaam}} //{{server}}/{{share_naam}} {{mountpoint}}`

- Maak verbinding als gastgebruiker (zonder wachtwoord):

`mount.cifs -o guest //{{server}}/{{share_naam}} {{mountpoint}}`

- Stel eigendomsinformatie in voor de mounted map:

`mount.cifs -o uid={{gebruiker_id|gebruikersnaam}},gid={{groep_id|groepsnaam}} //{{server}}/{{share_naam}} {{mountpoint}}`
