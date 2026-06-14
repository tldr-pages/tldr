#մոշ

> Mobile Shell-ը (`mosh`) SSH-ի ամուր և պատասխանատու փոխարինող է:.
> `mosh` պահպանում է կապերը հեռավոր սերվերների հետ ցանցերի միջև ռոումինգում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mosh>:.

- Միացեք հեռավոր սերվերին.:

`mosh {{username}}@{{remote_host}}`

- Միացեք որոշակի ինքնությամբ (մասնավոր բանալի) հեռավոր սերվերին.:

`mosh --ssh="ssh -i {{path/to/key_file}}" {{username}}@{{remote_host}}`

- Միացեք հեռավոր սերվերին, օգտագործելով հատուկ նավահանգիստ.:

`mosh --ssh="ssh -p {{2222}}" {{username}}@{{remote_host}}`

- Հեռավոր սերվերի վրա հրաման գործարկեք.:

`mosh {{remote_host}} -- {{command -with -flags}}`

- Ընտրեք Mosh UDP պորտը (օգտակար, երբ `remote_host`-ը NAT-ի հետևում է):

`mosh -p {{124}} {{username}}@{{remote_host}}`

- Օգտագործում, երբ `mosh-server` երկուականը ստանդարտ ճանապարհից դուրս է՝:

`mosh --server={{path/to/mosh-server}} {{remote_host}}`
