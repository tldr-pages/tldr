# msfconsole

> Վահանակով Metasploit Framework-ի համար:.
> Նշում․ գործարկեք `sudo msfdb init`-ը՝ Metasploit տվյալների բազան ակտիվացնելու համար, նախքան `msfconsole`-ը գործարկելը:.
> Լրացուցիչ տեղեկություններ. <https://docs.rapid7.com/metasploit/msf-overview/>:.

- Գործարկեք ինտերակտիվ վահանակը (ավելացրեք `--quiet`՝ գործարկման դրոշակը փակելու համար):

`sudo msfconsole`

- Կատարեք վահանակի հրամաններ (Նշում. օգտագործեք `;` մի քանի հրամաններ փոխանցելու համար).:

`sudo msfconsole {{[-x|--execute-command]}} "{{use auxiliary/scanner/portscan/tcp; set PORTS 80,443; set RHOSTS example.com; run; quit}}"`

- Գործարկել հատուկ ռեսուրսային ֆայլ.:

`sudo msfconsole {{[-r|--resource]}} {{path/to/file.rc}}`

- [Ինտերակտիվ] Ցուցադրել հատուկ տեսակի մոդուլներ.:

`show {{auxiliary|encoders|evasion|exploits|nops|payloads|post}}`

- [Ինտերակտիվ] Օգտագործեք մոդուլ.:

`use {{auxiliary/scanner/portscan/syn}}`

- [Ինտերակտիվ] Ցույց տալ մոդուլի ընտրանքները (մոդուլը նախ պետք է բեռնել).:

`show options`

- [Ինտերակտիվ] Փոփոխականի արժեքը.:

`set {{variable_name}} {{value}}`

- [Ինտերակտիվ] Գործարկեք մոդուլը (մոդուլը պետք է բեռնվի և նախ ընտրեք ընտրանքները).:

`{{run|exploit}}`
