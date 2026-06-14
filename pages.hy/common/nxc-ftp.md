# nxc ftp

> Pentest և շահագործել FTP սերվերները:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/ftp-protocol/password-spraying>:.

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Շարունակեք վավեր հավատարմագրերի որոնումը նույնիսկ վավեր հավատարմագրերը գտնելուց հետո.:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}} --continue-on-success`

- Կատարեք գրացուցակների ցանկեր յուրաքանչյուր FTP սերվերի վրա, որտեղ տրամադրված հավատարմագրերը վավեր են.:

`nxc ftp {{192.168.178.0/24}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --ls`

- Ներբեռնեք նշված ֆայլը թիրախային սերվերից.:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --get {{path/to/file}}`

- Վերբեռնեք նշված ֆայլը թիրախային սերվերին նշված վայրում.:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --put {{path/to/local_file}} {{path/to/remote_location}}`
