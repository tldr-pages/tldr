# smbmap

> Թվարկեք սամբայի համօգտագործվող կրիչներ ամբողջ տիրույթում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ShawnDEvans/smbmap#help>:.

- Թվարկեք հյուրընկալողներին միացված NULL նիստերով և բաց բաժնետոմսեր.:

`smbmap --host-file {{path/to/file}}`

- Ցուցադրել SMB-ի բաժնետոմսերը և թույլտվությունները [H]ost-ում՝ պահանջելով օգտվողի գաղտնաբառը կամ NTLM հեշը.:

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip_address}}`

- Կատարեք shell հրամանը հեռավոր համակարգում.:

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip_address}} -x {{command}}`

- Թվարկեք հյուրընկալողներին և ստուգեք SMB ֆայլի թույլտվությունները.:

`smbmap --host-file {{path/to/file}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -q`

- Միացեք ip-ին կամ հոսթին smb-ի միջոցով՝ օգտագործելով օգտվողի անուն և գաղտնաբառ.:

`smbmap {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain}} -H {{ip_or_hostname}}`

- Գտեք և ներբեռնեք ֆայլերը [R]էկուրսիվորեն մինչև `n` մակարդակների խորությունը՝ փնտրելով ֆայլի անվան օրինակ (`regex`) և բացառելով որոշ համօգտագործումներ.:

`smbmap --host-file {{path/to/file}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -q -R --depth {{n}} --exclude {{sharename}} -A {{filepattern}}`

- Վերբեռնեք ֆայլը smb-ի միջոցով՝ օգտագործելով օգտվողի անունը և գաղտնաբառը.:

`smbmap {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain}} -H {{ip_or_hostname}} --upload {{path/to/file}} '{{/share_name/remote_filename}}'`

- Ցուցադրել SMB բաժնետոմսերը և ռեկուրսիվորեն ցուցակագրել դիրեկտորիաներն ու ֆայլերը՝ փնտրելով `regex`-ին համապատասխանող ֆայլերի բովանդակություն:

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip_address}} -R -F {{pattern}}`
