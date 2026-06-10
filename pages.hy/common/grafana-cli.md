# grafana cli

> Կառավարեք Գրաֆանան:.
> Լրացուցիչ տեղեկություններ. <https://grafana.com/docs/grafana/latest/administration/cli/>:.

- Տեղադրեք հավելումներ.:

`grafana cli plugins install {{plugin_id1 plugin_id2 ...}}`

- Պլագին տեղադրելիս նշեք հիմնական ուղին.:

`grafana cli --homepath {{/usr/share/grafana}} plugins install {{plugin_id}}`

- Թարմացրեք պլագինները.:

`grafana cli plugins update {{plugin_id1 plugin_id2 ...}}`

- Հեռացնել պլագինները.:

`grafana cli plugins remove {{plugin_id1 plugin_id2 ...}}`

- Թվարկեք բոլոր տեղադրված պլագինները.:

`grafana cli plugins ls`
