# smbmap

> Lehetővé teszi a felhasználók számára, hogy egy teljes tartományon belül felsorolják a samba megosztott meghajtókat. További információ: <https://github.com/ShawnDEvans/smbmap>.

- NULL munkamenetekkel engedélyezett és nyitott megosztásokkal rendelkező hosztok felsorolása:

`smbmap --host-file {{path/to/file}}`

- Hostok felsorolása és SMB-fájljogosultságok ellenőrzése:

`smbmap --host-file {{path/to/file}} -u {{username}} -p {{password}} -q`

- Csatlakozás egy ip-hez vagy hostnévhez smb-n keresztül felhasználónév és jelszó használatával:

`smbmap -u {{username}} -p {{password}} -d {{domain}} -H {{ip_or_hostname}}`

- Fájlok keresése és letöltése \[R\]ecursively up to N levels depth, keresés fájlnévmintára (regex), és bizonyos megosztások kizárása:

`smbmap --host-file {{path/to/file}} -u {{username}} -p {{password}} -q -R --depth {{number}} --exclude {{sharename}} -A {{filepattern}}`

- Fájl feltöltése smb-n keresztül felhasználónév és jelszó használatával:

`smbmap -u {{username}} -p {{password}} -d {{domain}} -H {{ip_or_hostname}} --upload {{path/to/file}} '{{/share_name/remote_filename}}'`
