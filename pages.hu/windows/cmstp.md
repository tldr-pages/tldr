# cmstp

> Parancssori eszköz a kapcsolati szolgáltatási profilok kezelésére. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- Egy adott profil telepítése:

`cmstp "{{path/to/profile}}"`

- Telepítés asztali parancsikon létrehozása nélkül:

`cmstp /ns "{{path/to/profile}}"`

- Telepítés függőségek ellenőrzése nélkül:

`cmstp /nf "{{path/to/profile}}"`

- Csak az aktuális felhasználóhoz telepítés:

`cmstp /su "{{path/to/profile}}"`

- Telepítés minden felhasználó számára (rendszergazdai jogosultságokat igényel):

`cmstp /au "{{path/to/profile}}"`

- Telepítés némán, felszólítás nélkül:

`cmstp /s "{{path/to/profile}}"`

- Egy adott profil eltávolítása:

`cmstp /u "{{path/to/profile}}"`

- Eltávolítás csendben, megerősítő kérés nélkül:

`cmstp /u /s "{{path/to/profile}}"`
