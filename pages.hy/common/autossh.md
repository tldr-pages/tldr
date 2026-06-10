# autossh

> Գործարկեք, վերահսկեք և վերագործարկեք SSH կապերը:.
> Ավտոմատ կերպով միանում է նավահանգիստների վերահասցեավորման թունելները պահպանելու համար: Ընդունում է բոլոր SSH դրոշները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/autossh>:.

- Սկսեք SSH նստաշրջան՝ վերագործարկվելով, երբ [M] մոնիտորինգի նավահանգիստը չի կարողանում վերադարձնել տվյալները.:

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- Փոխանցեք [L]տեղական միացքը դեպի հեռավոր, անհրաժեշտության դեպքում վերագործարկեք.:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- SSH-ն գործարկելուց առաջ `autossh`-ը հետին պլան մղեք և մի բացեք հեռակա վահանակը.:

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- Գործարկեք հետին պլանում, առանց մոնիտորինգի միացքի, և փոխարենը ուղարկեք SSH պահվող փաթեթներ յուրաքանչյուր 10 վայրկյանը՝ ձախողումը հայտնաբերելու համար.:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- Աշխատեք հետին պլանում, առանց մոնիտորինգի միացքի և առանց հեռակառավարման վահանակի, դուրս գալով, եթե նավահանգիստը ձախողվի.:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Գործարկել հետին պլանում՝ գրանցելով `autossh` վրիպազերծման ելքը և SSH-ի բացահայտ ելքը ֆայլերին.:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}`
