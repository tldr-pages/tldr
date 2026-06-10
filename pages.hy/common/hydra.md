# հիդրա

> Առցանց գաղտնաբառի գուշակման գործիք:.
> Աջակցվող արձանագրությունները ներառում են FTP, HTTP(S), SMTP, SNMP, XMPP, SSH և այլն:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/hydra>:.

- Սկսեք Hydra's wizard-ը.:

`hydra-wizard`

- Գուշակիր SSH հավատարմագրերը, օգտագործելով տրված օգտվողի անունը և գաղտնաբառերի ցուցակը.:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- Գուշակիր HTTPS վեբ ձևի հավատարմագրերը՝ օգտագործելով օգտանունների և գաղտնաբառերի երկու հատուկ ցուցակներ («https_post_request» կարող է լինել «username=^USER^&password=^PASS^»):

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} {{host_ip}} {{https-post-form}} "{{url_without_host}}:{{https_post_request}}:{{login_failed_string}}"`

- Գուշակիր FTP-ի հավատարմագրերը՝ օգտագործելով օգտանունների և գաղտնաբառերի ցուցակները՝ նշելով շղթաների քանակը.:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- Գուշակիր MySQL հավատարմագրերը, օգտագործելով օգտվողի անունը և գաղտնաբառերի ցուցակը, դուրս գալով, երբ գտնվի օգտվողի անուն/գաղտնաբառ զույգ.:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- Գուշակիր RDP հավատարմագրերը, օգտագործելով օգտվողի անունը և գաղտնաբառերի ցուցակը, ցույց տալով յուրաքանչյուր փորձ.:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -V {{rdp://host_ip}}`

- Գուշակիր IMAP-ի հավատարմագրերը մի շարք հոսթերների վրա՝ օգտագործելով երկու կետով բաժանված օգտանունների/գաղտնաբառերի զույգերի ցանկը.:

`hydra -C {{path/to/username_password_pairs.txt}} {{imap://[host_range_cidr]}}`

- Գուշակիր POP3-ի հավատարմագրերը հոսթերների ցանկում, որոնք օգտագործում են օգտանունների և գաղտնաբառերի ցուցակները, դուրս գալով, երբ օգտանուն/գաղտնաբառ զույգ գտնվի.:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} -F {{pop3}}`
