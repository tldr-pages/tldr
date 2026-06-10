# jmtpfs

> FUSE-ի վրա հիմնված ֆայլային համակարգ MTP սարքեր մուտք գործելու համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/jmtpfs>:.

- Տեղադրեք MTP սարքը գրացուցակում.:

`jmtpfs {{path/to/directory}}`

- Սահմանեք տեղադրման ընտրանքները.:

`jmtpfs -o {{allow_other,auto_unmount}} {{path/to/directory}}`

- Ցուցակեք հասանելի MTP սարքերը.:

`jmtpfs {{[-l|--listDevices]}}`

- Եթե կան մի քանի սարքեր, տեղադրեք որոշակի սարք.:

`jmtpfs -device={{bus_id}},{{device_id}} {{path/to/directory}}`

- Ապամոնտաժել MTP սարքը.:

`fusermount -u {{path/to/directory}}`
