# ssh-copy-id

> Տեղադրեք ձեր հանրային բանալին հեռավոր մեքենայի autorized_keys-ում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ssh-copy-id>:.

- Պատճենեք ձեր բանալիները հեռավոր մեքենայի վրա.:

`ssh-copy-id {{username}}@{{remote_host}}`

- Պատճենեք տրված հանրային բանալին հեռակառավարման վրա.:

`ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}`

- Տրված հանրային բանալին պատճենեք հեռակառավարման վահանակին հատուկ պորտով.:

`ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}`
