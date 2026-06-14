# smbclient

> FTP-անման հաճախորդ՝ սերվերների վրա SMB/CIFS ռեսուրսներ մուտք գործելու համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/smbclient>:.

- Ցուցակեք հասանելի բաժնետոմսերը սերվերի վրա անանուն.:

`smbclient {{[-L|--list]}} {{server}} --no-pass`

- Միացեք բաժնետոմսին (գաղտնաբառ կպահանջվի).:

`smbclient //{{server}}/{{share}}`

- Միացեք բաժնետոմսին որպես հատուկ օգտվող.:

`smbclient {{[-U|--user]}} {{domain/username}} //{{server}}/{{share}}`

- Միացեք բաժնետոմսին որպես հատուկ օգտվող՝ ներկառուցված գաղտնաբառով.:

`smbclient {{[-U|--user]}} {{domain/username%password}} //{{server}}/{{share}}`

- Միացեք բաժնետոմսին հատուկ աշխատանքային խմբի միջոցով.:

`smbclient {{[-W|--workgroup]}} {{domain}} {{[-U|--user]}} {{username}} //{{server}}/{{share}}`

- Ներբեռնեք ֆայլ հատուկ գրացուցակից բաժնետոմսի վրա.:

`smbclient {{[-U|--user]}} {{domain/username}} //{{server}}/{{share}} {{[-D|--directory]}} {{path/to/directory}} {{[-c|--command]}} 'get {{filename}}'`

- Վերբեռնեք ֆայլ բաժնետոմսի հատուկ գրացուցակում.:

`smbclient {{[-U|--user]}} {{domain/username}} //{{server}}/{{share}} {{[-D|--directory]}} {{path/to/directory}} {{[-c|--command]}} 'put {{path/to/local_file}}'`
