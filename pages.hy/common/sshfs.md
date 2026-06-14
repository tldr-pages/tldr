# sshfs

> SSH-ի վրա հիմնված ֆայլային համակարգի հաճախորդ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/libfuse/sshfs/blob/master/sshfs.rst>:.

- Տեղադրեք հեռավոր գրացուցակը.:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- Ապամոնտաժել հեռավոր գրացուցակը.:

`umount {{mountpoint}}`

- Տեղադրեք հեռավոր գրացուցակը սերվերից հատուկ նավահանգիստով.:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- Օգտագործեք սեղմում.:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`

- Հետևեք խորհրդանշական հղումներին.:

`sshfs -o follow_symlinks {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`
