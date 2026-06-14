# mqtt_check.py

> MQTT մուտքի հավատարմագրերը փորձարկելու և վավերացնելու պարզ գործիք:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Ստուգեք MQTT մուտքի հավատարմագրերը թիրախի համար (MQTT բրոքերի հյուրընկալողի անունը).:

`mqtt_check.py {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Նույնականացման համար նշեք հատուկ հաճախորդի ID.:

`mqtt_check.py -client-id {{client_id}} {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Միացնել SSL կապի համար.:

`mqtt_check.py -ssl {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Միացեք որոշակի պորտին (կանխադրվածը 1883 է).:

`mqtt_check.py -port {{port}} {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Միացնել վրիպազերծման ելքը.:

`mqtt_check.py -debug {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Ցուցադրել օգնությունը.:

`mqtt_check.py --help`
