# scp

> Ապահով պատճեն:.
> Պատճենեք ֆայլերը հոսթերների միջև՝ օգտագործելով Secure Copy Protocol-ը SSH-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://man.openbsd.org/scp>:.

- Պատճենեք տեղական ֆայլը հեռավոր հոսթին.:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Հեռավոր հոսթին միանալիս օգտագործեք հատուկ նավահանգիստ.:

`scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Պատճենեք ֆայլը հեռավոր հոսթից տեղական գրացուցակում.:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Ռեկուրսիվ կերպով պատճենեք գրացուցակի բովանդակությունը հեռավոր հոսթից տեղական գրացուցակ.:

`scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Պատճենեք ֆայլ երկու հեռավոր հոսթների միջև, որոնք փոխանցվում են տեղական հոսթի միջոցով.:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}`

- Հեռավոր հոսթին միանալիս օգտագործեք հատուկ օգտվողի անուն.:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}`

- Օգտագործեք հատուկ SSH մասնավոր բանալի հեռավոր հոսթի հետ նույնականացման համար.:

`scp -i {{~/.ssh/private_key}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Հեռավոր հոսթին միանալիս օգտագործեք հատուկ վստահված անձ.:

`scp -J {{proxy_username}}@{{proxy_host}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`
