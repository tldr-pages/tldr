#չար շահագործում

> Windows Remote Management (WinRM) կեղև՝ pentesting-ի համար:.
> Միանալուց հետո մենք ստանում ենք PowerShell հուշում թիրախային հոսթի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Hackplayers/evil-winrm>:.

- Միացեք հյուրընկալողին և սկսեք ինտերակտիվ նիստ.:

`evil-winrm {{[-i|--ip]}} {{ip_address}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{password}}`

- Միացեք հոսթին՝ օգտագործելով «pas-the-hash» վավերացում՝ գաղտնաբառի փոխարեն.:

`evil-winrm {{[-i|--ip]}} {{ip_address}} {{[-u|--user]}} {{user}} {{[-H|--hash]}} {{nt_hash}}`

- Միացեք հոսթին՝ նշելով դիրեկտորիաներ PowerShell սկրիպտների և գործադիրների համար.:

`evil-winrm {{[-i|--ip]}} {{ip_address}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{password}} {{[-s|--scripts]}} {{path/to/scripts}} {{[-e|--executables]}} {{path/to/executables}}`

- Միացեք հոսթին, օգտագործելով SSL:

`evil-winrm {{[-i|--ip]}} {{ip_address}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{password}} {{[-S|--ssl]}} {{[-c|--pub-key]}} {{path/to/pubkey}} {{[-k|--priv-key]}} {{path/to/privkey}}`

- [Ինտերակտիվ] Վերբեռնեք ֆայլ հոսթին.:

`upload {{path/to/local_file}} {{path/to/remote_file}}`

- [Ինտերակտիվ] Ցուցակեք բոլոր բեռնված PowerShell գործառույթները.:

`menu`

- [Ինտերակտիվ] Բեռնել PowerShell սկրիպտը `--scripts` գրացուցակից.:

`{{script.ps1}}`

- [Ինտերակտիվ] Հրավիրեք երկուական հոսթին `--executables` գրացուցակից.:

`Invoke-Binary {{binary.exe}}`
