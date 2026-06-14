# ամպամած

> Ստեղծեք մշտական կապ Cloudflare ցանցի հետ:.
> Լրացուցիչ տեղեկություններ. <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>:.

- Նույնականացրեք և կապեք կապը տիրույթի հետ Cloudflare հաշվում.:

`cloudflared tunnel login`

- Ստեղծեք թունել հատուկ անունով.:

`cloudflared tunnel create {{name}}`

- Թվարկեք հաշվի բոլոր թունելները.:

`cloudflared tunnel list`

- Ստեղծեք DNS CNAME գրառում, որը ցույց է տալիս թունելը.:

`cloudflared tunnel route dns {{name|uuid}} {{hostname}}`

- Պահպանեք տեղեկամատյանները ֆայլում.:

`cloudflared tunnel --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}} run {{name}}`

- Գործարկել անունով թունել (կարդում է կոնֆիգուրացիան `config.yml`-ից):

`cloudflared tunnel run {{name}}`

- Սկսեք ժամանակավոր թունել՝ տեղական ծառայությունը բացահայտելու համար (հաշիվ չի պահանջվում).:

`cloudflared tunnel --url http://localhost:{{port}}`

- Տեղադրեք cloudflared-ը որպես համակարգի ծառայություն.:

`cloudflared service install`
