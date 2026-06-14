# kdeconnect-cli

> Օգտագործեք KDE Connect-ը՝ սարքի հետ ֆայլեր կամ տեքստեր համօգտագործելու, դրա համար զանգահարելու, ապակողպելու և շատ ավելին:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/kdeconnect-cli>:.

- Նշեք բոլոր սարքերը.:

`kdeconnect-cli {{[-l|--list-devices]}}`

- Ցանկ մատչելի (զուգակցված և հասանելի) սարքեր.:

`kdeconnect-cli --list-available`

- Հայցեք զուգակցում կոնկրետ սարքի հետ՝ նշելով դրա ID-ն.:

`kdeconnect-cli --pair --device {{device_id}}`

- Զանգահարեք սարքին՝ նշելով դրա անունը.:

`kdeconnect-cli --ring --name "{{device_name}}"`

- Կիսվեք URL-ով կամ ֆայլով զուգակցված սարքի հետ՝ նշելով դրա ID-ն.:

`kdeconnect-cli --share {{url|path/to/file}} --device {{device_id}}`

- Ուղարկեք SMS կամընտիր հավելվածով որոշակի համարին.:

`kdeconnect-cli --name "{{device_name}}" --send-sms "{{message}}" --destination {{phone_number}} --attachment {{path/to/file}}`

- Բացեք որոշակի սարք.:

`kdeconnect-cli --name "{{device_name}}" --unlock`

- Ստիպել ստեղնաշարի սեղմումը կոնկրետ սարքի վրա.:

`kdeconnect-cli --name "{{device_name}}" --send-keys {{key}}`
