# pg_receivewal

> Հեռարձակեք նախօրոք գրելու գրանցամատյանը գործող PostgreSQL կլաստերից:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgreceivewal.html>:.

- Ուղարկել WAL-ը տեղական գրացուցակ (նվազագույնը պահանջվում է).:

`pg_receivewal {{[-D|--directory]}} {{directory}}`

- Նույնը, ինչ վերևում, նշեք հոսթ, նավահանգիստ, օգտվողի անունը, ներառյալ բառացի ելքը.:

`pg_receivewal {{[-v|--verbose]}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-D|--directory]}} {{directory}}`

- Օգտագործեք կրկնօրինակման բնիկ (ստեղծեք, եթե անհրաժեշտ է).:

`pg_receivewal {{[-S|--slot]}} {{slot_name}} --create-slot {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}} {{[-D|--directory]}} {{directory}}`

- Կանգնեք տվյալ WAL դիրքում (LSN).:

`pg_receivewal {{[-E|--endpos]}} {{lsn}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Վերահսկիչ շրջադարձ ձախողման դեպքում.:

`pg_receivewal {{[-n|--no-loop]}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Տվյալները համաժամանակյա լվացեք (ստիպեք WAL-ին անմիջապես գրել).:

`pg_receivewal --synchronous {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Սեղմել WAL ելքը (`gzip`, մակարդակ 0-9):

`pg_receivewal {{[-Z|--compress]}} {{level|method}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`

- Սահմանեք կարգավիճակի հաշվետվության միջակայքը.:

`pg_receivewal {{[-s|--status-interval]}} {{seconds}} {{[-D|--directory]}} {{directory}} {{[-h|--host]}} {{host}} {{[-p|--port]}} {{port}} {{[-U|--username]}} {{username}}`
