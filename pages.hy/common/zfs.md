# zfs

> Կառավարեք ZFS ֆայլային համակարգերը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zfs>:.

- Թվարկեք բոլոր հասանելի zfs ֆայլային համակարգերը.:

`zfs list`

- Ստեղծեք նոր ZFS ֆայլային համակարգ.:

`zfs create {{pool_name/filesystem_name}}`

- Ջնջել ZFS ֆայլային համակարգը.:

`zfs destroy {{pool_name/filesystem_name}}`

- Ստեղծեք ZFS ֆայլային համակարգի պատկեր.:

`zfs snapshot {{pool_name/filesystem_name}}@{{snapshot_name}}`

- Միացնել սեղմումը ֆայլային համակարգի վրա.:

`zfs set compression=on {{pool_name/filesystem_name}}`

- Փոխել տեղադրման կետը ֆայլային համակարգի համար.:

`zfs set mountpoint=/{{path/to/mount_point}} {{pool_name/filesystem_name}}`
